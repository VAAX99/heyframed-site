---
type: reference
aliases: ["Framed Workflows", "Framed n8n"]
created: 2026-03-21
modified: 2026-03-21
up: "[[_Framed-Project]]"
tags: [framed, n8n, workflows, reference]
---

# ⚙️ Framed — n8n Workflow Reference

---

## Anime Daily Workflow (`0qEMmLaonjcOVDGZ`)

**Trigger:** Every Day at 7:00 AM

**Full Node Pipeline:**
1. Fetch ANN News RSS
2. Prepare Date Variables
3. AniList — Today's Anniversaries (graphql.anilist.co)
4. AniList — Current Trending
5. AniList — This Week's Airing (Pages 1-3)
6. Merge all sources
7. Story Selection Logic (dedup + future episode filter + air time priority)
8. Check Story History (read Google Sheets)
9. Pass History to Selection → all fields required (L10)
10. Fetch TMDB Image (romajiTitle first, english fallback)
11. Fetch TMDB Backdrops
12. Select Best Backdrop
13. Cloudinary Upload (c_fill, g_auto:subject, ar_16:9, cloud: ddlmwfeup)
14. Cloudinary Detect Focal Point
15. Calculate Text Corner
16. OpenAI Generate Caption (<=120 chars, news-headline style)
17. Sanitize Caption
18. Build Bannerbear Payloads
19. Bannerbear Render Image (POST api.bannerbear.com/v2/images)
20. Wait 15 Seconds
21. Bannerbear Fetch Result
22. Download Final Image
23. Download Clean Image
24. Route by Size (from Config tab)
25. Save Wallpaper [size] (Google Drive upload per size)
26. Update Description [size] (Google Drive file metadata)
27. Mark Story as Delivered
28. Log Story to Sheet (append Google Sheets)
29. Fetch Active Sizes
30. Get Active Subscribers (read Google Sheets)
31. Send Wallpaper DM (Telegram sendPhoto per subscriber)
32. Post [size] (Telegram sendPhoto to channel)

**Known dedup bug:** Date serial number issue — see [[_Framed-Lessons]] L13

---

## Space Daily Workflow (`uOdTPWr3VXmQW51B`)

**Trigger:** Every Day at 7:30 AM

**Current Node Pipeline (basic):**
1. NASA — Fetch APOD (GET api.nasa.gov/planetary/apod)
2. Check Space History (read Google Sheets)
3. Dedup Check → Is New? (true/false)
4. Build Space Caption
5. Download Space Image
6. Post to Telegram — Space (sendPhoto)
7. Log Space Story (append Google Sheets)

**Missing vs Anime workflow:**
- ❌ media_type filter (NASA APOD can return videos)
- ❌ Cloudinary focal point crop
- ❌ OpenAI caption generation
- ❌ Bannerbear rendering (no overlay/branding)
- ❌ Multi-size routing (Config tab)
- ❌ Google Drive save
- ❌ Subscriber DM delivery
- ❌ ISO date storage (serial number bug same as anime)

**Space Story Log sheet ID:** `1OAHxIvFWw82dKdKMzh2gxgPKx8g_QroVpfhRvV9tZs8`
**Space Drive folder:** `1lloa6sWYptniWOiO4Swy_c7skd7LmWDL`

---

## Stripe Webhook Handler (`ITEVAJkboWsaANvQ`)

**Trigger:** POST Webhook (`/webhook/stripe-framed`)

**Pipeline:**
1. Parse Stripe event
2. Is New Sub? → Extract New Subscriber → Upsert to Google Sheets
3. Is Cancellation? → Extract Cancellation → Set active=false

**Stripe event types handled:**
- `checkout.session.completed` → new subscriber
- `customer.subscription.deleted` → cancellation

---

## Bannerbear Payload Structure

```javascript
// Build Bannerbear Payload (from anime workflow)
{
  template: templateId,  // from Config tab
  modifications: [
    {
      name: "background",      // layer name in template
      image_url: cloudinaryUrl  // processed image from Cloudinary
    },
    {
      name: "caption",          // text layer
      text: sanitizedCaption
    }
  ],
  webhook_url: null,  // polling used instead
  transparent: false
}
```

**API endpoint:** `POST https://api.bannerbear.com/v2/images`
**Auth:** Bearer token (stored in n8n Bannerbear credential)
**Poll endpoint:** `GET https://api.bannerbear.com/v2/images/{uid}`
**Wait strategy:** Wait 15s node → Bannerbear Fetch Result node

---

## NASA APOD API

**Endpoint:** `GET https://api.nasa.gov/planetary/apod`
**Key params:** `api_key`, `date` (YYYY-MM-DD, defaults to today)
**Returns:**
- `media_type`: "image" or "video" — ALWAYS check this before downloading
- `url`: image URL (or YouTube embed if video)
- `hdurl`: high-res image URL (use this when available)
- `title`: image title
- `explanation`: long description
- `copyright`: photographer credit (may be empty for NASA-owned images)
- `date`: YYYY-MM-DD string

**Free tier:** 1000 requests/day
**Fallback for video days:** Request `?date=yesterday` or use a NASA Image Library search
