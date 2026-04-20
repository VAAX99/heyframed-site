# Framed Project — Credentials Access Guide

> All agents should read this before requesting credentials from the board.
> You have access to the credentials below. Use them autonomously.

---

## Where Are the Credentials?

All credentials for the Framed project are stored in:

```
E:\paperclip\_SAFE_LOCAL\
```

Files in that folder:

| File | Contents |
|------|----------|
| `credentials.md` | n8n API key, n8n credential IDs (OpenAI, fal.ai, Replicate, Stability AI, Bannerbear), production workflow ID |
| `N8N API KEY 2026-03-23.txt` | Raw n8n Cloud API key (use `X-N8N-API-KEY` header) |
| `Telegram Chat Bots.txt` | Telegram bot tokens for Framed delivery |
| `github n8n token.txt` | GitHub token for n8n workflow access |
| `CLAUDE.md` | General project notes |
| `FRAMED_TODO.md` | Outstanding manual action items |

---

## How to Use Them

### n8n API (workflow read/write)

```
Base URL: https://framed.app.n8n.cloud
Auth header: X-N8N-API-KEY: <key from N8N API KEY 2026-03-23.txt>
```

Example — get a workflow:
```
GET https://framed.app.n8n.cloud/api/v1/workflows/0qEMmLaonjcOVDGZ
```

Known workflow IDs (also in `credentials.md`):
- `0qEMmLaonjcOVDGZ` — Space Daily (production)
- `ujmcMYDfRNHMG3CR` — AI Image Test

### n8n Credential IDs (internal, safe to reference in workflow JSON)

These are IDs stored inside n8n, not raw secrets:
- OpenAI: `uGJTm7rByVrIiCUx`
- fal.ai: `bAXH8BCqbEEB6RhE`
- Replicate: `HL3f6h3DopDo0rMh`
- Stability AI: `r2zZUiOgzLaF9jiZ`
- Bannerbear template: `97xPQmDnqx6Y5G3E82`

### Telegram Bot

Read `E:\paperclip\_SAFE_LOCAL\Telegram Chat Bots.txt` for the bot token.
Use the Telegram Bot API with `sendPhoto` / `sendMessage` to deliver content.

### Google Sheets (subscriber data)

- Spreadsheet ID: `129SQgeuJTl9Mrncc7h2H8JbCIHFZrEW0ARDZXcvjCvM`
- OAuth2 credential is stored inside n8n (credential ID: `4XYaxeIOLcSZ6D1L`)
- Access it via n8n workflow nodes, not directly from agent code

---

## Rules

- **Read credentials from file; never hardcode them or write them into workflow JSON**.
- **Never commit or expose credentials in comments, issue descriptions, or code.**
- **If a credential seems expired or incorrect, post a comment on your task and ask the board to rotate it.** Do not guess or try alternatives.
- **Do not wait for the board to provide credentials that already exist in `_SAFE_LOCAL`.** Check that folder first.

---

## Who Needs What

| Agent | Credentials Needed |
|-------|--------------------|
| n8nSpecialist | n8n API key, n8n credential IDs, workflow IDs |
| CTO | n8n API key (for oversight), Google Sheets ID (for planning) |
| SecOps | None stored here — uses browser-based audit tools |
| QA | None stored here — uses browser automation |
| TTS | None stored here — uses web research tools |
| UXDesigner | None stored here — works on local HTML files |

---

## Last Updated

April 18, 2026
