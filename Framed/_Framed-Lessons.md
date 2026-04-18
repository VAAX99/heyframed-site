---
type: note
aliases: ["Framed Lessons", "Framed lessons.md"]
created: 2026-03-21
modified: 2026-03-21
up: "[[_Framed-Project]]"
tags: [framed, lessons, reference]
---

# 📚 Framed — Lessons Learned

> [!WARNING] Read at session start
> Review all lessons before working on Framed to avoid repeating mistakes.

---

**L1 — Always work in framed.daily@gmail.com (u/1)**
Before creating any Google file, verify the blue "A" avatar is active. Use `/u/1/` in all Google URLs. Personal account = profile photo = WRONG.

**L2 — n8n connections must be name-keyed, not ID-keyed**
When patching workflow JSON via API, always use the node display name as the connection key (e.g. "Select Best Backdrop"), never the UUID.

**L3 — n8n $() references require a graph edge**
`$('NodeName')` only works if that node is in the upstream path. For parallel branches, restructure sequentially or accept the limitation.

**L4 — Google Sheets node caches column schema**
After any column reorder, rebuild `parameters.columns.schema[]` via API to match new order. Node does not auto-detect schema changes.

**L5 — Google Drive docs are the source of truth (instructions, context, lessons)**
Update Instructions doc and Project Context in Drive first. Local files are secondary only.

**L6 — Read CLAUDE.md and lessons.md at session start**
Non-negotiable. Context summary may be stale. Drive docs are authoritative.

**L7 — Context summary ≠ reading the actual docs**
Always navigate to and READ the files. Don't rely on what was summarized.

**L8 — Adding a task about something ≠ doing the thing**
If a doc needs to be filled, fill it that session. Don't substitute a reminder for the work.

**L9 — Update logs at ~90% token usage**
When approaching 90% context: (1) update Wallpaper Project Log, (2) mark completed tasks in Instructions, (3) note exact next step.

**L10 — Pass History nodes must forward ALL fields, not just the ID**
Story Selection Logic filters with `new Date(r.date) > cutoff`. If `r.date` is undefined, comparison is always false → recentIds always empty → any show can repeat.
Fix: `const items = $input.all().map(i => i.json); return [{ json: { historyRows: items } }];`

**L11 — Always set `operation: "read"` explicitly on Google Sheets read nodes**
When building via API, always include `operation: "read"` in parameters.

**L12 — Each category is fully isolated**
Space gets its own Drive folder + its own spreadsheet + its own n8n workflow. Never mix categories in the same spreadsheet.

**L13 — Google Sheets stores dates as Excel serial numbers**
Dates like `46097` are Excel serials (days since 1899-12-30). `new Date(46097)` = Jan 1, 1970, NOT March 2026.
Fix: `new Date((serialDate - 25569) * 86400 * 1000)` OR store as ISO strings ("2026-03-16").

**L14 — NASA APOD sometimes returns videos, not images**
Always check `media_type === "image"` before downloading. On video days, fall back to previous day's APOD.

**L15 — Bannerbear silently ignores wrong layer names — always verify from a working execution**
If a layer name is wrong, Bannerbear renders the template blank WITHOUT any error. Status = "completed", image_url exists, but the image is empty.
Fix: Before writing a new Bannerbear payload, extract `modifications[].name` from a real WORKING execution to get the exact layer names. Never guess or assume names like "background" or "caption" — always confirm.
Real names for template `97xPQmDnqx6Y5G3E82`: `background_image`, `caption_text`, `caption_box`.

**L16 — n8n execution logs use deduped JSON (reference arrays)**
`GET /rest/executions/{id}?includeData=true` returns `data.data` as a string containing a deduped JSON array.
Structure: `arr[0]` = root with string refs → resolve by index. `arr[4]` is usually `runData` keyed by node name.
Find the node names index with: `arr.findIndex(item => Object.keys(item||{}).some(k => k.includes('YourNodeName')))`

**L17 — Always diagnose a failure before rebuilding — check execution logs first**
When something doesn't work: pull the execution data BEFORE changing anything. You need to know WHAT failed and WHY, not just assume. In the blank Bannerbear case, the payload was correct — only the layer names were wrong. A 5-minute diagnosis saved a full rebuild.

**L19 — Bannerbear CACHES the last render values per layer — always reset ALL layers**
If you send wrong layer names, Bannerbear renders using the previous render's cached values for those layers. A space workflow that sends `background` (wrong) instead of `background_image` (correct) will get the PREVIOUS ANIME render's background image and caption.
Fix: Always send modifications for ALL layers in the template, including ones you want empty (use `text: " "` for text layers to clear them).
Template `97xPQmDnqx6Y5G3E82` layers to always include: `background_image`, `caption_text`, `episode_list`, `caption_box`.

**L20 — Use Claude Vision for automated image quality verification**
Instead of just checking `status === "completed"` (which passes even on blank renders), call the Anthropic API with the rendered image and ask Claude to verify the content. Model: `claude-haiku-4-5`. If FAIL → alert admin via personal Telegram bot, do NOT push to public channel.
Alexandre's personal Telegram chat ID: `7418222966` | Bot credential: `Jj9vE6TWwCQhGLAN` (Telegram MyAssistant_Alexb_Bot).

**L18 — Verification checks must catch the actual failure mode**
A verification step that checks `status === "completed"` AND `image_url` exists would NOT have caught the blank Bannerbear render — both were true even when the image was blank. Verification must check the thing that can actually fail. For Bannerbear: verify layer names match the template BEFORE sending.

**L21 — NEVER hardcode Telegram bot tokens in HTTP Request nodes**
File_ids in Telegram are bot-specific. If the hardcoded token in `getFile` is for a DIFFERENT bot than the one that received the webhook, the API returns `400 Bad Request: wrong file_id` — no other indication of the mismatch. This can silently exist for months.
Fix: Use the Telegram Trigger's `additionalFields.download: true` option instead. n8n downloads the photo automatically using the credential's token (always correct). Parse Caption then passes the binary through. No token ever touches the workflow code.
Bonus: `$credentials.accessToken` does NOT work in n8n HTTP Request URL expressions for Telegram — predefinedCredentialType does not inject into URL path.
