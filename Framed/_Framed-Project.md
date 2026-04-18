---
type: project
aliases: ["Framed", "Wallpaper Project", "heyframed"]
created: 2026-03-21
modified: 2026-03-21
up: "[[_Business-MOC]]"
tags: [project, business, framed, wallpaper, active]
status: active
---

# 🖼️ Framed — Daily Wallpaper Service

> [!INFO] What is Framed?
> Daily cinematic wallpaper service delivered via Telegram DM. Powered by n8n Cloud.
> Website: [heyframed.com](https://heyframed.com) | Drive: framed.daily@gmail.com (u/1)

---

## 🎯 Current Status

| Item | Status |
|------|--------|
| Anime workflow | ✅ Active (FHD daily, dedup fixed) |
| Space workflow | ✅ Active (FHD + Bannerbear + OpenAI, published 2026-03-21) |
| Landing page | ✅ Live at heyframed.com |
| Stripe | ✅ Links live |
| Subscribers | 0 (no marketing yet) |
| Marketing | ❌ Not started (IP issue with anime) |

**Pivot decision (2026-03-13):** Space = primary category (NASA public domain, no IP risk). Anime kept for Telegram channel but NOT for paid subscriptions.

---

## 💰 Business Model

| Tier | Price | Features |
|------|-------|----------|
| Free | $0 | Daily FHD wallpaper via Telegram channel |
| Framed | $4.99/mo | FHD/2K/4K/Phone/Tablet, 1 category, DM delivery |
| Framed+ | $9.99/mo | All categories per-device, all sizes, archive, auto-change app |
| Bundles | $9.99 one-time | Themed packs (30 wallpapers) |

**Money path:** Landing page → Subscriptions → Marketing → New categories

---

## 🔑 Key IDs & References

### n8n Workflows
| Workflow | ID | Status |
|----------|-----|--------|
| Anime Daily ("My workflow") | `0qEMmLaonjcOVDGZ` | ✅ Active |
| Space Daily | `uOdTPWr3VXmQW51B` | ⚠️ Needs fixes |
| Stripe Webhook Handler | `ITEVAJkboWsaANvQ` | ✅ Active |
| AI Image Test | `ujmcMYDfRNHMG3CR` | ❌ Inactive |

### Google Sheets (framed.daily@gmail.com)
| File | ID |
|------|-----|
| Anime Story Log | `129SQgeuJTl9Mrncc7h2H8JbCIHFZrEW0ARDZXcvjCvM` |
| Space Story Log | `1OAHxIvFWw82dKdKMzh2gxgPKx8g_QroVpfhRvV9tZs8` |
| Config tab GID | `495589417` |

### Google Drive Folders
| Folder | ID |
|--------|-----|
| Anime parent | `1yBQivvU5gz5GSeLVltojGoepq_-YHWet` |
| Anime Tagged | `1jS5D60TuL5NogTx1KkGU7lMG_WAz8DMf` |
| Anime Clean | `15VMaVvGgHYIu19WrlEK6t49bnAauRAZW` |
| Space parent | `1lloa6sWYptniWOiO4Swy_c7skd7LmWDL` |

### Bannerbear Templates
| Size | Template ID | Status |
|------|-------------|--------|
| Desktop FHD (1920×1080) | `97xPQmDnqx6Y5G3E82` | ✅ Active |
| Desktop QHD (2560×1440) | `gwNr4n50xPdA5ROMBd` | Ready (inactive) |
| Phone Portrait (1080×1920) | `nxOjMA5gQvGgbprE63` | Ready (inactive) |
| 4K / Ultrawide / Tablet | — | Not built yet |

### Stripe
| Item | ID |
|------|-----|
| Framed price | `price_1T93NZ3JAJzIMzIJya59R3Fj` |
| Framed+ price | `price_1T93Nw3JAJzIMzIJZXm9IiBA` |
| Subscribers sheet tab / GID | `406792303` |
| Webhook URL | `https://framed.app.n8n.cloud/webhook/stripe-framed` |

### Google Docs (framed.daily@gmail.com)
| Doc | ID |
|-----|-----|
| Instructions (master todo) | `1AYw93e_O22HKAK4EbBWLKGaHDjkn2cL5LLoNHvn2LGQ` |
| Wallpaper Project Context | `1-SzQ7U7m8H06w4wTRWtu9_duRezixXdZc_1lzfv-8zA` |
| CLAUDE.md | `1oOrgCXrUavoEHgzhi-jK9v43rIC4iuZmd7wlbyFQLrI` |
| lessons.md | `1N-u9Hb825IwRi_mFVlyqUED3OZlZQLBTWM85-vLqytE` |
| Wallpaper Project Log | `1bUPVzAFgKf_7RnwMmBscS-xa91KA97XlCvrpgSO3n-Q` |

---

## 🏗️ Architecture

```
NASA APOD API / AniList API
        ↓
   Story Selection (dedup vs Story Log)
        ↓
   TMDB / APOD backdrop fetch
        ↓
   Cloudinary (focal point crop → 16:9)
        ↓
   OpenAI caption generation
        ↓
   Bannerbear (FHD overlay + branding)
        ↓
   Google Drive (Clean + Tagged folders)
        ↓
   Google Sheets log
        ↓
   Telegram (channel post + subscriber DMs)
```

---

## 🐛 Known Bugs

### 1. Anime dedup — date serial number bug ✅ FIXED (2026-03-21)
**Root cause:** Google Sheets stores dates as Excel serial numbers (e.g. `46097`). JavaScript's `new Date(46097)` = Jan 1, 1970, NOT March 2026.
**Fix applied:** Story Selection Logic now uses `(typeof row.date === 'number' ? new Date((row.date - 25569) * 86400 * 1000) : new Date(row.date))`.

### 2. Space workflow — incomplete ✅ FIXED (2026-03-21)
**Fix applied:** Full pipeline added — media_type filter, OpenAI caption, Bannerbear FHD render, Google Drive save, ISO date logging, Telegram post. Workflow published and active.

---

## 📋 Next Actions

### High Priority
- [x] Fix Space Daily workflow (Bannerbear FHD, media_type filter, dedup date format)
- [x] Fix anime dedup date serial bug
- [ ] Move to Space as primary free tier (update landing page)
- [ ] Marketing launch after Space stable

### Medium Priority
- [ ] Set up Stripe account properly + test end-to-end checkout
- [ ] Build Subscribers tab in Space Story Log
- [ ] Add social media publish toggle to n8n (before Reddit/Instagram)
- [ ] Confirm subscriber-triggered size routing only enables extra wallpaper sizes when demand exists

### Low Priority
- [ ] QHD / Phone Portrait size activation (flip Config tab)
- [ ] 4K / Ultrawide / Tablet Bannerbear templates
- [ ] Migrate subscribers tracking to Supabase (from Google Sheets)
