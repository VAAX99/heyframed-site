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

#### Accessibility Requirements (WCAG 2.1 AA)
- **Text Contrast:** Minimum 4.5:1 ratio for normal text, 3:1 for large text (7:1 for AAA)
- **Interactive Elements:** Must meet minimum 3:1 contrast against background
- **Touch Target Size:** Minimum 44×44px for all interactive elements (iOS) / 48×48dp (Material Design)
- **Touch Spacing:** Minimum 8px gap between adjacent touch targets
- **Color Independence:** Never convey information by color alone—always include text/icons
- **Dark Mode Compliance:** Maintain contrast ratios in both light and dark themes
- **Focus Indicators:** Visible 2-4px focus rings on interactive elements with proper contrast
- **Screen Reader Support:** All images have descriptive `alt` attributes, icon-only buttons have `aria-label`
- **Keyboard Navigation:** Tab order matches visual order, all interactive elements reachable
- **Reduced Motion:** Respect `prefers-reduced-motion` setting, provide static alternatives
- **Skip Links:** "Skip to main content" for keyboard users
- **Semantic HTML:** Use proper heading hierarchy (h1→h6), `button` elements, form labels
- **Error Recovery:** Clear error messages with recovery paths, inline validation after blur

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

**Icon System:**
- **Style:** Consistent stroke width (1.5-2px), geometric, minimal fills
- **Library:** Heroicons or Lucide for systematic consistency
- **Sizes:** 16px (small), 20px (default), 24px (large), 32px (hero)
- **States:** Default, hover, active, disabled with consistent opacity/color changes
- **Accessibility:** All decorative icons have `aria-hidden="true"`, functional icons have labels

**Common Icons:**
- ✦ (Sparkle/Star) — Used for premium features, bullet points (decorative only)
- Vector equivalents for UI:
  - Mobile/Device icon — Subscription/delivery (`aria-label="Device delivery"`)
  - Clock/Sun icon — Daily delivery concept (`aria-label="Daily delivery"`)
  - Sparkle vector — Transformation/magic (`aria-label="Premium feature"`)
  - Picture Frame vector — Core brand symbol (`aria-label="Framed logo"`)
  - Download icon — Archive access (`aria-label="Download wallpaper"`)
  - Settings icon — Preferences (`aria-label="Settings"`)
  - Check icon — Confirmation states (`aria-label="Completed"`)
  - Arrow icons — Navigation (`aria-label="Next page"` or `aria-label="Previous page"`)

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

### Performance Guidelines (Core Web Vitals)
- **Image Optimization:** Use WebP/AVIF formats, responsive images with `srcset`, lazy load non-critical assets
- **Font Loading:** `font-display: swap` to prevent FOIT, preload critical fonts only
- **Critical CSS:** Inline above-the-fold styles, defer below-fold CSS
- **Layout Stability:** Declare image dimensions, reserve space for async content (CLS < 0.1)
- **Bundle Optimization:** Route-level code splitting, dynamic imports for heavy features
- **Main Thread Budget:** Keep per-frame work under 16ms for 60fps smooth interactions
- **Input Latency:** Provide visual feedback within 100ms of user interactions
- **Loading States:** Show skeleton/shimmer for operations exceeding 300ms
- **Third-party Scripts:** Load async/defer, audit performance impact regularly
- **Debounce/Throttle:** Use for high-frequency events (scroll, resize, input)
- **Intersection Observer:** Use for scroll-based animations and lazy loading

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
- **Sizes:** 40px (small), 52px (default), 58px (large) - all meet 44px minimum touch target
- **Touch Targets:** Extend hit area beyond visual bounds if needed for 44×44px minimum
- **Semantic HTML:** Always use `button` element, never `div` with click handlers
- **Accessibility:** Icon-only buttons require `aria-label`, disabled state uses `disabled` attribute
- **States:** default, hover (`translateY(-1px)` + glow), active, disabled (opacity: 0.38), loading
- **Loading Feedback:** Disable during async operations, show spinner, preserve button width
- **Animation:** 150-300ms transitions, honor `prefers-reduced-motion`
- **Keyboard Support:** Visible focus rings, Space/Enter activation
- **Touch Feedback:** Subtle scale (0.95-1.05) on press for mobile

**Cards:**
- **Border Radius:** 10px (default), 16px (large), consistent with design system
- **Elevation:** Subtle borders (`--border`), hover shadow elevation for depth
- **Hover States:** `scale(1.03)`, accent border, elevated shadow, 150-300ms transition
- **Aspect Ratios:** Use CSS `aspect-ratio` property for consistent proportions
- **Content Handling:** Truncate with ellipsis, provide expand/tooltip for full content
- **Interactive States:** Clear visual feedback, maintain accessibility contrast
- **Touch Targets:** Entire card clickable with proper focus management
- **Loading States:** Skeleton placeholder during content load

**Forms & Inputs:**
- **Labels:** Always visible with `for` attribute, never placeholder-only
- **Error Handling:** Inline messages below fields, clear recovery paths
- **Validation:** On blur (not keystroke), real-time for critical fields
- **Accessibility:** Proper `autocomplete`, `aria-describedby` for helper text
- **Focus States:** Visible 2-4px rings with proper contrast ratios
- **Required Fields:** Asterisk indicators, `required` attribute for screen readers
- **Helper Text:** Persistent below complex inputs, not just placeholders
- **Input Types:** Semantic types (email, tel, number) for mobile keyboards
- **Touch Targets:** Minimum 44px height for mobile usability
- **Progressive Disclosure:** Complex options revealed as needed, not overwhelming upfront

**Animations:**
- **Duration:** 150-300ms for micro-interactions, max 400ms for complex transitions
- **Easing:** ease-out for entering, ease-in for exiting, spring physics for natural feel
- **Performance:** Animate `transform`/`opacity` only, avoid layout-triggering properties
- **Accessibility:** Honor `prefers-reduced-motion`, provide static alternatives
- **Specificity:** Never `transition: all` - always specify exact properties
- **Purpose:** Every animation must convey meaning, not just decoration
- **Interruption:** All animations must be interruptible by user input
- **Continuity:** Maintain spatial relationships during transitions
- **Loading States:** Progress indicators for operations >300ms
- **State Changes:** Smooth transitions between hover/active/disabled states

**Responsive Design:**
- **Mobile-First:** Design for 375px base, progressively enhance for larger screens
- **Breakpoints:** 375px (mobile), 768px (tablet), 1024px (desktop), 1440px (large)
- **Container:** Max-width 1160px with 24px horizontal padding, fluid scaling
- **Touch Spacing:** Minimum 8px between interactive elements, 44×44px touch targets
- **Typography Scale:** Responsive font sizes using `clamp()` for fluid scaling
- **Line Length:** 35-60 characters mobile, 60-75 desktop for optimal readability
- **Viewport:** `width=device-width, initial-scale=1` - never disable zoom
- **Layout:** No horizontal scroll, flexible grid systems, proper content priority
- **Safe Areas:** Respect device safe areas for notch/gesture navigation
- **Orientation:** Maintain usability in both portrait and landscape modes

### Interaction Patterns

**Touch & Gestures:**
- **Touch Targets:** Minimum 44×44px (iOS) / 48×48dp (Android) for all interactive elements
- **Touch Feedback:** Visual response within 100ms, subtle scale/ripple effects
- **Gesture Support:** Standard platform gestures (swipe-back, pinch-zoom) without conflicts
- **Hover vs Touch:** Primary interactions use tap/click, don't rely on hover alone
- **Multi-Touch:** Support standard gestures, avoid conflicting gesture regions

**Navigation Patterns:**
- **Predictable Back:** Consistent back navigation behavior, preserve state/scroll position
- **Deep Linking:** All key screens accessible via URL for sharing and bookmarking
- **Breadcrumbs:** Use for hierarchies 3+ levels deep on web
- **Focus Management:** After navigation, move focus to main content for accessibility
- **Loading Transitions:** Skeleton screens for >300ms loads, preserve spatial continuity

**Feedback Systems:**
- **Loading States:** Skeleton UI, progress indicators, disable controls during async operations
- **Error Recovery:** Clear messages with specific recovery actions, not generic "error occurred"
- **Success Feedback:** Brief confirmation (toast, checkmark, color change) for completed actions
- **Empty States:** Helpful guidance and clear next steps when no content exists
- **Undo Support:** Provide undo for destructive actions (delete, bulk operations)

**Progressive Enhancement:**
- **Core Functionality:** Works without JavaScript for critical paths
- **Graceful Degradation:** Features degrade elegantly when resources unavailable
- **Offline Support:** Basic functionality available offline with clear status indication
- **Network Awareness:** Adapt interface for slow/unstable connections

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

**Accessibility (WCAG 2.1 AA):**
- [ ] All interactive elements have minimum 44×44px touch targets
- [ ] Form inputs include proper labels and autocomplete attributes  
- [ ] Icon-only buttons have descriptive `aria-label` attributes
- [ ] Focus states are visible (2-4px rings) for keyboard navigation
- [ ] Text contrast meets 4.5:1 minimum (7:1 for AAA)
- [ ] Color is not the only way to convey information
- [ ] Images include descriptive `alt` attributes and explicit dimensions
- [ ] Heading hierarchy follows logical order (h1→h6, no skipping)
- [ ] Skip links provided for keyboard users
- [ ] Screen reader tested with actual assistive technology

**Performance & Core Web Vitals:**
- [ ] Images optimized (WebP/AVIF), responsive with `srcset`
- [ ] Critical CSS inlined, non-critical deferred
- [ ] Layout shift (CLS) < 0.1 with reserved spaces for dynamic content
- [ ] Loading states for operations >300ms with skeleton/spinner UI
- [ ] Main thread budget <16ms per frame for 60fps interactions
- [ ] Third-party scripts loaded async/defer, impact audited

**Interaction & Usability:**
- [ ] Animations respect `prefers-reduced-motion` setting
- [ ] Touch feedback provided within 100ms of user interaction
- [ ] Error messages are inline with clear recovery paths
- [ ] Loading states disable controls and show clear progress
- [ ] Back navigation preserves state and scroll position
- [ ] Empty states provide helpful guidance and next steps
- [ ] Undo functionality for destructive actions

**Technical Implementation:**
- [ ] Semantic HTML used (`button`, `a`, `label`, proper landmarks)
- [ ] Progressive enhancement: core functionality works without JS
- [ ] Responsive design tested at all major breakpoints
- [ ] Cross-browser compatibility verified (Chrome, Firefox, Safari, Edge)
- [ ] Mobile testing on actual devices, not just desktop simulation

### Quality Standards

**Content Quality:**
- All images must be 16:9 aspect ratio for consistent delivery
- Minimum resolution 1920×1080 (FHD) for standard tier
- Higher resolutions available: 2560×1440 (QHD), 3840×2160 (4K)
- Focal point optimization using Cloudinary auto-detection for smart cropping
- Brand overlay positioned intelligently to avoid obscuring key visual elements
- Caption length ≤120 characters for optimal Telegram display

**Technical Quality:**
- Image compression optimized for quality/size balance (WebP/AVIF preferred)
- Color profile consistency (sRGB) across all content
- Metadata preservation for attribution and organization
- Deduplication systems to prevent repeated content
- Version control for content updates and corrections

**Brand Consistency:**
- Visual style matching established content categories
- Consistent caption formatting and voice
- IP compliance verification for all paid tier content
- Quality assurance review before publication
- Performance monitoring for delivery speed and reliability

### Approval Process
- Content curation follows established principles
- New categories require brand consistency review
- Marketing materials maintain voice and visual standards
- Partnership content aligns with brand values

---

## Document History

**Version 2.0** - April 18, 2026
- Enhanced accessibility guidelines to WCAG 2.1 AA standards
- Added comprehensive interaction patterns and modern UX guidelines
- Expanded performance guidelines with Core Web Vitals focus
- Updated component specifications with detailed accessibility requirements
- Added progressive enhancement and technical quality standards

**Version 1.0** - March 2026
- Initial comprehensive brand guide
- Established design system and visual identity
- Content guidelines and business model documentation

---

*For questions about brand implementation, consult the UX Designer or project lead.*
*This document serves as the single source of truth for Framed brand implementation.*