# 🖼️ Framed — Brand Identity Guide

> **Your Story, Delivered Daily**

---

## Brand Overview

**Framed** is a daily wallpaper delivery service that transforms your screen into a storytelling canvas. We deliver cinematic, high-quality wallpapers via Telegram, focusing on anime and space imagery that tells compelling visual stories.

### Mission Statement
To bring daily visual storytelling to your digital life through carefully curated, cinematic wallpapers that inspire and connect with your personal narrative.

### Brand Taglines
**Primary Tagline:** "Your Story, Delivered Daily"
- Used on landing page title and primary marketing
- Emphasizes the daily delivery value proposition
- Matches live website implementation

**Supporting Line:** "Your story, framed."
- Used for brand reinforcement and secondary messaging
- Emphasizes the storytelling and framing concept
- Complements the primary tagline

### Brand Positioning
- **Premium accessibility:** High-quality content delivered through familiar platforms
- **Story-first curation:** Every image chosen for its narrative impact, not just aesthetics
- **Effortless experience:** No apps, no accounts—just quality delivered daily

---

## Visual Identity

### Logo & Wordmark

**Primary Logo:** `FRAMED` 
- Typography: Inter, 700 weight, uppercase, letter-spacing: 0.12em
- The "D" appears in accent color (#F0B429)
- Format: `FRAME<span style="color: #F0B429;">D</span>`

**Usage Guidelines:**
- Always maintain consistent letter spacing (0.12em)
- The accent "D" should never appear in standard text color
- Logo scales well from 15px (footer) to 18px (navigation)

### Color Palette

#### Primary Colors
```css
--accent:        #F0B429  /* Gold/Yellow - Primary brand color */
--bg:            #0d1117  /* Deep dark background */
--text:          #e6edf3  /* Primary text */
```

#### Extended Palette
```css
--surface:       #161b22  /* Card/surface backgrounds */
--surface-raised:#1c2230  /* Elevated surfaces */
--accent-dim:    #c99320  /* Hover states */
--accent-subtle: rgba(240,180,41,0.10)  /* Subtle backgrounds */
--accent-glow:   rgba(240,180,41,0.25)  /* Glow effects */
--text-secondary:#8b949e  /* Secondary text */
--text-muted:    #3d444d  /* Muted text */
--border:        rgba(255,255,255,0.10)  /* Default borders */
--border-accent: rgba(240,180,41,0.35)   /* Accent borders */
```

#### Color Psychology
- **Gold/Yellow (#F0B429):** Premium, warmth, creativity, optimism
- **Deep Dark (#0d1117):** Sophistication, focus, cinematic quality
- **Clean Whites:** Clarity, simplicity, premium feel

#### Accessibility Requirements
- **Text Contrast:** Minimum 4.5:1 ratio for normal text, 3:1 for large text
- **Interactive Elements:** Must meet minimum 3:1 contrast against background
- **Color Independence:** Never convey information by color alone—always include text/icons
- **Dark Mode Compliance:** Maintain contrast ratios in both light and dark themes
- **Focus Indicators:** Visible focus states for keyboard navigation

### Typography

**Primary Font:** Inter
- Sans-serif typeface chosen for modern readability
- Available weights used: 300, 400, 500, 600, 700, 800
- Excellent screen rendering across all devices
- Variable font support for better performance

**Hierarchy:**
- **Hero Headlines:** 300 weight, large scale (44px-80px), minimal letter-spacing (-0.03em), line-height: 1.05
- **Section Titles:** 700 weight, medium scale (28px-42px), tight letter-spacing (-0.02em), line-height: 1.15
- **Body Text:** 400-500 weight, readable scale (16px base/14px-17px mobile), line-height: 1.6
- **UI Elements:** 600 weight, small scale (11px-15px), wide letter-spacing (0.12-0.18em), uppercase

**Typography Guidelines:**
- Minimum 16px body text on mobile (prevents iOS auto-zoom)
- Use `…` not `...` for truncation and loading states
- Apply `text-wrap: balance` on headings to prevent widows
- Use `font-variant-numeric: tabular-nums` for data comparisons

### Iconography

**Icon Style:**
- Minimal, geometric approach
- Single-color fills using brand colors
- 16px-24px standard sizing
- SVG format for scalability and theming
- Consistent stroke width (1.5px-2px)

**Usage Guidelines:**
- Use SVG icons, never emojis for UI elements
- Icon-only buttons require `aria-label` attributes
- Decorative icons need `aria-hidden="true"`
- Minimum 44×44px touch targets on interactive icons
- Maintain visual consistency with same icon family (Heroicons, Lucide)

**Common Icons:**
- ✦ (Sparkle/Star) — Used for premium features, bullet points
- Vector equivalents for UI:
  - Mobile/Device icon — Subscription/delivery
  - Clock/Sun icon — Daily delivery concept  
  - Sparkle vector — Transformation/magic
  - Picture Frame vector — Core brand symbol

---

## Voice & Tone

### Brand Voice Characteristics

**Cinematic:** Language that evokes visual storytelling and cinematic experiences
- ✅ "Every frame tells a story"
- ✅ "Cinematic wallpaper service"
- ✅ "Your story, framed"

**Accessible:** Friendly, straightforward, no jargon
- ✅ "No app. No account. Just open Telegram"
- ✅ "Three steps. That's it."
- ✅ "Free forever"

**Premium but approachable:** Quality-focused without being pretentious
- ✅ "Hand-picked moments"
- ✅ "Delivered daily"
- ❌ "Luxury wallpaper experience" (too pretentious)

### Tone Variations

**Marketing Copy:** Confident, aspirational, benefit-focused
- "Transform your screen into a storytelling canvas"
- "Ready for a better wallpaper?"

**Product Descriptions:** Clear, feature-focused, honest
- "Standard sizes, your chosen category, delivered to your Telegram daily"
- "No account required for the free channel"

**UI/UX Copy:** Minimal, functional, helpful
- "Continue to checkout"
- "See recent drops"
- "Browse Packs"

---

## Content Guidelines

### Content Categories

**Primary: Space**
- NASA APOD sourcing for copyright safety and public domain compliance
- Emphasize cosmic beauty, scale, and scientific wonder
- Scientific accuracy in descriptions and captions
- Current status: Active (free and paid tiers)
- Strategic priority: No IP risks, suitable for monetization

**Secondary: Anime**
- Focus on cinematic moments from popular series
- Prioritize visual storytelling over action scenes
- Include episode context when relevant
- Current status: Active (free Telegram channel only)
- IP Constraint: Not used for paid subscriptions due to copyright risks
- Pivot Decision (2026-03-13): Moved to secondary due to IP concerns

**Planned Categories:**
- Cars, Nature, Architecture, Sci-Fi, Landscapes
- Cyberpunk, Fantasy Art, Dark Academia
- Unlock based on subscriber growth

### Content Curation Principles

1. **Story First:** Every image should tell or suggest a narrative
2. **Cinematic Quality:** Wide aspect ratio (16:9), high production value
3. **Emotional Impact:** Images that evoke feeling and connection
4. **Technical Excellence:** Proper focal points, clean composition
5. **Brand Safety:** Respect IP when possible, prioritize public domain

### Caption Style

**Format:** News-headline style, ≤120 characters
**Examples:**
- "Attack on Titan · Ep. 87"
- "Nebula Series · No. 12"
- "Epic Vistas · No. 7"

**Guidelines:**
- Concise and informative
- Include series/source when relevant
- Use middle dot (·) as separator
- Maintain consistent numbering for series

---

## Business Model & Positioning

### Pricing Strategy Philosophy
- **Free tier excellence:** Genuinely valuable free offering
- **Clear upgrade value:** Obvious benefits for paid tiers
- **Fair pricing:** Comparable to other subscription services

### Customer Journey
1. **Discovery:** Free Telegram channel
2. **Engagement:** Daily wallpaper habit formation
3. **Upgrade consideration:** Need for higher resolution/more control
4. **Retention:** Consistent quality and new features

### Value Propositions

**Free Tier:**
- "Everything you need to start—no card, no catch"
- Daily FHD delivery via Telegram
- Forever free promise

**Framed ($4.99/mo):**
- Multi-resolution support
- Category choice
- Direct message delivery

**Framed+ ($9.99/mo):**
- All categories, per-device customization
- Full archive access
- Auto-change app (planned)

---

## Brand Applications

### Digital Presence

**Website (heyframed.com):**
- Dark theme with cinematic feel
- Hero background: High-quality space/landscape imagery
- Consistent use of reveal animations
- Mobile-first responsive design

**Telegram Channel:**
- Daily posts with consistent formatting
- Professional channel description
- High-quality image previews

### Marketing Materials

**Social Proof Elements:**
- "200+ wallpapers delivered"
- "Free forever"
- "1920 × 1080 HD"
- "No account required for free"

**Call-to-Action Language:**
- Primary: "See plans" / "Continue to checkout"
- Secondary: "See recent drops" / "Browse Packs"
- Telegram-specific: "Join Free on Telegram"

### Email/Communication Templates

**Onboarding:**
- Welcome message emphasizing story/quality
- Clear next steps for setup
- Feature highlights with visual examples

**Feature Announcements:**
- New category launches
- Resolution/size additions
- App releases

---

## Brand Extensions & Future

### Planned Features
- **Auto-change apps:** Desktop wallpaper automation
- **Wallpaper packs:** Themed collections ($9.99 one-time)
- **Multi-device sync:** Different categories per device
- **Archive access:** Full historical library

### Partnership Opportunities
- **Content creators:** Anime studios for official content
- **Platforms:** Desktop wallpaper apps, mobile launchers
- **Hardware:** Desktop/mobile OEM partnerships

### Brand Expansion Guidelines
- Maintain core "daily story" concept
- Keep delivery mechanism simple and familiar
- Preserve free tier value proposition
- Scale categories based on demand validation

---

## Technical Brand Implementation

### Performance Guidelines
- **Image Optimization:** Use WebP/AVIF formats, responsive images with `srcset`
- **Font Loading:** `font-display: swap` to prevent invisible text
- **Critical CSS:** Inline critical styles, defer non-critical CSS  
- **Lazy Loading:** Use `loading="lazy"` for below-fold images
- **Bundle Optimization:** Split code by route, dynamic imports for heavy components
- **Layout Stability:** Declare image dimensions to prevent CLS
- **Third-party Scripts:** Load async/defer, audit regularly for necessity

### Design Tokens (CSS Custom Properties)
```css
:root {
  --bg: #0d1117;
  --surface: #161b22;
  --surface-raised: #1c2230;
  --accent: #F0B429;
  --accent-dim: #c99320;
  --accent-subtle: rgba(240,180,41,0.10);
  --accent-glow: rgba(240,180,41,0.25);
  --text: #e6edf3;
  --text-secondary: #8b949e;
  --text-muted: #3d444d;
  --border: rgba(255,255,255,0.10);
  --border-accent: rgba(240,180,41,0.35);
  --font: 'Inter', sans-serif;
  --radius-sm: 6px;
  --radius: 10px;
  --radius-lg: 16px;
  --transition: 0.2s ease;
}
```

### Component Guidelines

**Buttons:**
- Height: 40px (small), 52px (default), 58px (large)
- Minimum 44×44px touch targets for mobile accessibility
- Use `button` element, never `div` with click handlers
- Include `aria-label` for icon-only buttons
- States: default, hover, active, disabled, loading
- Loading state: disable during async operations with spinner
- Hover: `transform: translateY(-1px)` with glow effect

**Cards:**
- Border radius: 10px (default), 16px (large)
- Subtle borders using `--border` color token
- Hover states: scale(1.03), border accent, elevated shadow
- Maintain aspect ratios with CSS aspect-ratio property
- Handle content overflow with truncation or scrolling

**Forms & Inputs:**
- Labels visible (not placeholder-only)
- Error messages inline below fields
- Autocomplete attributes for better UX
- Focus states with `focus-visible:ring-*` styling
- Required field indicators (asterisk)
- Helper text for complex inputs

**Animations:**
- Duration: 150-300ms for micro-interactions
- Easing: ease-out for entering, ease-in for exiting
- Honor `prefers-reduced-motion` setting
- Animate `transform`/`opacity` only for performance
- Never `transition: all` - specify properties

**Responsive Design:**
- Mobile-first approach: design for 375px then scale up
- Breakpoints: 375px (mobile), 768px (tablet), 1024px (desktop), 1440px (large)
- Container max-width: 1160px with 24px horizontal padding
- Touch-friendly spacing: minimum 8px between interactive elements
- Readable line lengths: 35-60 characters mobile, 60-75 desktop
- Viewport meta tag: `width=device-width, initial-scale=1`
- No horizontal scroll on any breakpoint

---

## Brand Management

### Consistency Checklist
- [ ] Logo uses correct accent color for "D"
- [ ] Color values match brand palette exactly
- [ ] Typography hierarchy follows guidelines
- [ ] Voice matches brand characteristics
- [ ] Content meets curation principles
- [ ] CTAs use approved language

### UI/UX Implementation Checklist
- [ ] All interactive elements have minimum 44×44px touch targets
- [ ] Form inputs include proper labels and autocomplete attributes
- [ ] Icon-only buttons have `aria-label` attributes
- [ ] Focus states are visible for keyboard navigation
- [ ] Animations respect `prefers-reduced-motion` setting
- [ ] Text contrast meets WCAG 2.1 AA standards (4.5:1)
- [ ] Semantic HTML used (`button`, `a`, `label`, proper headings)
- [ ] Images include `alt` attributes and explicit dimensions
- [ ] Loading states show progress indicators for operations >300ms
- [ ] Error messages are inline and include recovery guidance

### Quality Standards
- All images must be 16:9 aspect ratio
- Minimum resolution 1920×1080 for delivery
- Focal point optimization for various crops
- Brand overlay consistent across all wallpapers
- Caption length ≤120 characters

### Approval Process
- Content curation follows established principles
- New categories require brand consistency review
- Marketing materials maintain voice and visual standards
- Partnership content aligns with brand values

---

*Last updated: April 18, 2026*
*For questions about brand implementation, consult the UX Designer or project lead.*