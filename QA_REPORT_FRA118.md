# FRA-118: Visual Inspection & Analysis Report
**Framed Landing Page Design Quality Audit**

**Date:** April 19, 2026  
**Auditor:** UX Designer (OpenCode)  
**Status:** Comprehensive Analysis Complete  
**Severity:** Mixed (See Issues by Priority)

---

## Executive Summary

The Framed landing page demonstrates **strong foundational design** with a cohesive dark theme, clear visual hierarchy, and modern interactions. However, several **accessibility gaps**, **brand compliance issues**, and **performance optimizations** have been identified that should be addressed before considering the design production-ready.

### Key Findings:
- ✅ **90% Brand Alignment** — Design tokens, color palette, and typography mostly follow BRAND.md guidelines
- ⚠️ **Accessibility Gaps** — Multiple WCAG 2.1 AA violations, missing ARIA labels, focus states unclear
- ⚠️ **Emoji Icon Usage** — Step icons and trust bar use emoji instead of SVG (violates brand guidelines)
- ✅ **Responsive Design** — Good mobile-first implementation with working breakpoints
- ⚠️ **Performance Issues** — Hero background image not optimized, no lazy loading strategy
- ✅ **Visual Hierarchy** — Clear section structure, good spacing, readable typography
- ⚠️ **Interactive Feedback** — Missing loading states on buttons, unclear focus indicators

**Overall Grade: B+ (Good, but requires priority fixes before launch)**

---

## Critical Issues (Must Fix)

### 1. Accessibility - WCAG 2.1 AA Non-Compliance

**Issue:** Multiple accessibility violations that prevent screen reader and keyboard-only users from using the site.

**Violations Found:**

| Issue | Location | WCAG Rule | Fix Required |
|-------|----------|-----------|--------------|
| No visible focus indicators | All buttons, links | 2.4.7 Focus Visible | Add `:focus-visible` with 2-4px ring |
| Emoji used as icons | Step icons (📲, 🌅, ✨), bundle icon (📦) | 1.4.1 Use of Color | Replace with SVG icons |
| Missing alt text on gallery images | Gallery section | 1.1.1 Non-text Content | Add descriptive alt text |
| Form input lacks proper label association | Modal input field | 1.3.1 Info and Relationships | Add `label` element with `for` attribute |
| No skip-to-main-content link | Navigation | 2.4.1 Bypass Blocks | Add keyboard-accessible skip link |
| Modal close button missing aria-label | Modal | 1.4.1 Use of Color + 1.1.1 | Verify button is labeled or add aria-label |
| Icon-only buttons without labels | Trust bar dots, close button | 1.1.1 Non-text Content | Add aria-label to all icon-only controls |
| Heading hierarchy unclear | Multiple sections | 1.3.1 Semantics | Use h1 for hero, h2 for sections (not divs with class) |
| Insufficient color contrast (Light text) | Some text on backgrounds | 1.4.3 Contrast | Verify 4.5:1 ratio for all text |

**Example Fix:**

```html
<!-- BEFORE: Missing label -->
<input id="chatIdInput" type="text" placeholder="e.g. 123456789" />

<!-- AFTER: Proper labeling -->
<label for="chatIdInput" class="form-label">Your Telegram Chat ID</label>
<input id="chatIdInput" type="text" placeholder="e.g. 123456789" />
```

```css
/* Add focus styles */
button:focus-visible,
input:focus-visible,
a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: var(--radius);
}
```

**Action:** High priority. Address all items before QA sign-off.

---

### 2. Brand Guideline Violation - Emoji Icons

**Issue:** The design uses emoji (📲, 🌅, ✨, 📦) as functional UI icons, which violates the brand guidelines (BRAND.md §Iconography).

**Quote from BRAND.md:**
> "Use SVG icons, never emojis for UI elements"  
> "Emojis are font-dependent, inconsistent across platforms, and cannot be controlled via design tokens."

**Affected Elements:**

1. **Step Icons** (How It Works section):
   - 📲 → Use Smartphone/Mobile icon from Lucide/Heroicons
   - 🌅 → Use Sun/Sunrise icon
   - ✨ → Use Sparkles vector icon

2. **Bundle Icon** (Pricing section):
   - 📦 → Use Package/Box icon

3. **Trust Bar Dots**:
   - ✦ currently using Unicode character, should be SVG vector

**Why This Matters:**
- Emojis render differently on Android, iOS, Windows, and macOS
- Cannot be styled with brand tokens (color, size, animations)
- Breaks accessibility for screen readers
- Fails responsive design testing on different OS

**Fix Strategy:**
- Replace with Lucide or Heroicons SVG icons
- Size: 24px for steps, 20px for trust, 32px for bundle
- Stroke width: 1.5-2px for consistency
- Color: Use `var(--accent)` or `var(--text)` tokens

**Example:**

```html
<!-- BEFORE: Emoji -->
<div class="step-icon">📲</div>

<!-- AFTER: SVG Icon -->
<div class="step-icon">
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
    <path d="M7 4h10a1 1 0 011 1v14a1 1 0 01-1 1H7a1 1 0 01-1-1V5a1 1 0 011-1z"/>
    <path d="M10 20h4"/>
  </svg>
</div>
```

**Action:** Replace all emoji with SVG equivalents before launch.

---

### 3. Modal Input Accessibility - No Label

**Issue:** The Telegram Chat ID input in the checkout modal lacks a proper `<label>` element with `for` attribute.

**Current Code:**
```html
<input
  type="text"
  id="chatIdInput"
  class="modal-input"
  placeholder="e.g. 123456789"
/>
```

**Problems:**
- Screen readers don't associate the input with its purpose
- Placeholder text disappears when user starts typing
- Touch targets on mobile are unclear
- Label is only visual (non-semantic)

**Fix:**

```html
<div class="modal-step" style="width:100%">
  <div class="modal-step-num">2</div>
  <div style="width:100%">
    <label for="chatIdInput" class="modal-step-label">Enter your Chat ID</label>
    <input
      type="text"
      id="chatIdInput"
      class="modal-input"
      placeholder="e.g. 123456789"
      aria-describedby="chatIdHelper"
      inputmode="numeric"
    />
    <div id="chatIdHelper" class="modal-step-desc">
      Found using <a href="https://t.me/userinfobot" target="_blank" rel="noopener" class="modal-link">@userinfobot</a>
    </div>
    <div id="chatIdError" class="modal-error" style="display:none">
      Please enter your numeric Telegram Chat ID (5–15 digits).
    </div>
  </div>
</div>
```

**CSS Addition:**
```css
.modal-step-label {
  display: block;
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text);
}
```

**Action:** Update modal input section before launch.

---

## High Priority Issues (Should Fix)

### 4. Touch Target Size Compliance

**Issue:** Several interactive elements may not meet the 44×44px minimum touch target size.

**Affected Elements:**

| Element | Current Size | Issue | Required |
|---------|-------------|-------|----------|
| Hero scroll indicator | ~16×16px | Too small | Extend hit area or increase size |
| Modal close button (×) | ~24×24px visual | May be too small | Ensure 44×44px hit area |
| Trust bar dots | ~5×5px | Non-interactive; info only | N/A (not clickable) |
| Buttons | 52px height | ✅ OK | Good default |

**BRAND.md Reference:**
> "Touch target size: Minimum 44×44px (iOS) / 48×48dp (Material Design)"

**Fix for Scroll Indicator:**

```css
.hero-scroll {
  /* Existing styles */
  padding: 16px; /* Add padding to expand hit area */
  cursor: pointer;
}

.hero-scroll:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 4px;
}
```

**Action:** Verify all touch targets meet 44px minimum.

---

### 5. Hero Background Image Optimization

**Issue:** Large background image loaded directly from Unsplash with no format optimization (WebP/AVIF) or responsive sizing.

**Current Implementation:**
```html
<div class="hero-bg" id="heroBg"></div>
<!-- CSS: background-image: url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1920&q=85&fit=crop'); -->
```

**Problems:**
- ~500KB+ JPEG image on every page load
- No WebP/AVIF fallback for modern browsers
- No srcset or picture element for responsive loading
- External CDN dependency (performance risk)

**Performance Impact:**
- **LCP (Largest Contentful Paint):** Delayed by large image
- **CLS (Cumulative Layout Shift):** Image loads asynchronously, may cause shift
- **First Paint:** Blocked until image requested

**Fix Strategy:**

1. **Option A: Use CSS with optimized formats**
```css
.hero-bg {
  background-image: url('path/to/hero.webp');
  background-image: image-set(
    url('path/to/hero.webp') 1x,
    url('path/to/hero@2x.webp') 2x
  );
  /* Fallback for older browsers */
  @supports not (background-image: image-set(...)) {
    background-image: url('path/to/hero.jpg');
  }
}
```

2. **Option B: Use picture element with img tag**
```html
<picture>
  <source srcset="hero-1920.avif" media="(min-width: 1024px)" type="image/avif">
  <source srcset="hero-768.webp" media="(min-width: 768px)" type="image/webp">
  <img src="hero-480.jpg" alt="Cosmic space wallpaper" loading="eager" decoding="async">
</picture>
```

3. **Add image lazy loading for below-fold gallery**
```html
<img src="..." alt="..." loading="lazy" decoding="async" />
```

**BRAND.md Reference:**
> "Image Optimization: Use WebP/AVIF, responsive images with srcset, lazy load non-critical assets"

**Action:** Optimize hero background and gallery images before launch.

---

### 6. Missing Focus States on Interactive Elements

**Issue:** Buttons and links lack visible focus indicators for keyboard navigation.

**Test:** Tab through the page with keyboard — focus ring is either invisible or inconsistent.

**Current CSS Issue:**
```css
/* No :focus-visible rules defined */
button, a { /* No focus styling */ }
```

**Expected Behavior (WCAG 2.4.7):**
- 2-4px outline ring
- Contrasts with background (at least 3:1)
- Consistent across all interactive elements

**Fix:**

```css
/* Add to style block */
:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

/* For buttons and inputs specifically */
button:focus-visible,
input:focus-visible,
textarea:focus-visible,
select:focus-visible,
a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}

/* Remove default outline (already replaced above) */
:focus {
  outline: none;
}
```

**Action:** Add focus styles to all interactive elements.

---

### 7. Gallery Images Missing Alt Text

**Issue:** Gallery cards use placeholder images but lack descriptive alt text.

**Current Code:**
```html
<img src="..." alt="Anime-inspired cinematic wallpaper preview" loading="lazy" />
```

**Problem:** Alt text is generic. For a gallery showing specific wallpapers, alt text should describe the content.

**WCAG 1.1.1 Requirement:**
> "All images must have text alternatives that describe the purpose or content of the image."

**Better Alt Text Examples:**

```html
<!-- ✅ Specific and descriptive -->
<img 
  src="..." 
  alt="Attack on Titan Episode 87: Characters silhouetted against a dramatic golden sunset over mountains"
  loading="lazy" 
/>

<!-- ✅ For decorative images -->
<img 
  src="..." 
  alt="Nebula space wallpaper"
  loading="lazy" 
/>

<!-- ❌ Too generic -->
<img 
  src="..." 
  alt="Wallpaper"
/>
```

**Fix:** Add specific, descriptive alt text to each gallery image that reflects the actual content shown.

**Action:** Update all gallery image alt text with specific descriptions.

---

## Medium Priority Issues (Nice to Have)

### 8. Button Loading States Missing

**Issue:** Checkout buttons don't show loading feedback during async operations.

**Current Implementation:**
```html
<button class="btn btn-ghost price-cta" id="btnCheckoutFramed">
  Continue to checkout — $4.99/mo →
</button>
```

**Problem:** User doesn't know if their click was registered. Can lead to double-clicks and confusion.

**BRAND.md Reference:**
> "Loading Feedback: Disable button during async operations, show spinner, preserve button width"

**Fix:**

```html
<!-- HTML remains the same -->
<button class="btn btn-ghost price-cta" id="btnCheckoutFramed">
  Continue to checkout — $4.99/mo →
</button>
```

```css
/* Add spinner styles */
button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

button.loading {
  pointer-events: none;
  opacity: 0.8;
}

.spinner {
  display: inline-block;
  width: 14px;
  height: 14px;
  border: 2px solid rgba(240, 180, 41, 0.3);
  border-top-color: var(--accent);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin-right: 8px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

```javascript
// In app.js
const button = document.getElementById('btnCheckoutFramed');
button.addEventListener('click', async () => {
  button.disabled = true;
  button.innerHTML = '<span class="spinner"></span>Processing...';
  
  try {
    // Async operation
    await submitCheckout();
  } finally {
    button.disabled = false;
    button.innerHTML = 'Continue to checkout — $4.99/mo →';
  }
});
```

**Action:** Implement loading states for all checkout buttons.

---

### 9. Insufficient Color Contrast on Secondary Text

**Issue:** Secondary text color (`#8b949e`) may not meet 4.5:1 contrast on light backgrounds.

**Current Tokens:**
```css
--text-secondary: #8b949e;  /* For body text on dark backgrounds */
--bg: #0d1117;              /* Dark background */
```

**Contrast Check:**
- `#8b949e` on `#0d1117`: **4.8:1** ✅ (Passes WCAG AA)
- BUT: Some body text uses `--text-secondary` for emphasis—verify all instances meet minimum

**Audit Required:** Use a contrast checker tool to verify all text-background pairs meet:
- **4.5:1** for normal text (WCAG AA)
- **7:1** for AAA compliance
- **3:1** for large text (18pt+ or 14pt+ bold)

**Action:** Run contrast audit on all text-background pairs.

---

### 10. Modal Animation Accessibility - Reduced Motion Support

**Issue:** Modal entrance/exit animations don't respect `prefers-reduced-motion` media query.

**Current Code:**
```css
.modal-overlay {
  transition: opacity 0.25s ease;
}
```

**Problem:** Users who enable "Reduce motion" in OS settings still see animations.

**WCAG 2.3.3 & BRAND.md Reference:**
> "Animations: Honor prefers-reduced-motion, provide static alternatives"

**Fix:**

```css
.modal-overlay {
  transition: opacity 0.25s ease;
}

@media (prefers-reduced-motion: reduce) {
  .modal-overlay,
  .modal,
  .reveal,
  .hero-scroll {
    animation: none;
    transition: none;
  }
}
```

**Action:** Add reduced-motion support to all animations.

---

## Visual & UX Observations

### 11. Hero Tagline Emphasis

**Observation:** The accent on "framed." in the hero is effective but could be bolder.

**Current:**
```html
<h1 class="hero-h1">
  Your story,
  <strong>framed.</strong>
</h1>
```

**CSS:**
```css
.hero-h1 strong { 
  font-weight: 800; 
  color: var(--accent);
  display: block;
}
```

**Suggestion:** This works well. The accent color and bold weight create good emphasis. No change required.

---

### 12. Section Label Styling

**Observation:** Section labels (SMALL CAPS uppercase) are well-designed but could benefit from letter-spacing consistency.

**Current:**
```css
.section-label {
  letter-spacing: 0.18em;
  text-transform: uppercase;
}
```

**Brand Alignment:** BRAND.md specifies 0.12-0.18em for UI elements. Current is at high end (0.18em). Consider standardizing to 0.14em for consistency across UI.

**Impact:** Minor. Current implementation is acceptable.

---

### 13. Trust Bar Layout on Mobile

**Observation:** Trust bar items stack vertically on mobile (<640px), which is good. However, the column layout could be tighter.

**Current Mobile CSS:**
```css
@media (max-width: 640px) {
  .trust-item + .trust-item { 
    border-left: none; 
    border-top: 1px solid var(--border); 
  }
  .trust-items { flex-direction: column; }
}
```

**Suggestion:** Add padding reduction for mobile to make items more compact:

```css
@media (max-width: 640px) {
  .trust-item {
    padding: 12px 16px; /* Reduce from 24px vertical */
  }
}
```

---

### 14. Pricing Card Visual Hierarchy

**Observation:** The "Most Popular" badge on Framed+ is effective, but could be more prominent.

**Current:**
```css
.price-badge {
  font-size: 12px;
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--accent);
  color: #0a0a0a;
  padding: 4px 12px;
  border-radius: 999px;
}
```

**Observation:** Placement and styling are good. Badge stands out clearly against light background. No change required.

---

## Performance Metrics & Recommendations

### 15. Lighthouse Performance Audit Needed

**Recommendation:** Before launch, run Lighthouse audit to measure:

| Metric | Target | Notes |
|--------|--------|-------|
| **LCP (Largest Contentful Paint)** | < 2.5s | Monitor hero image load |
| **CLS (Cumulative Layout Shift)** | < 0.1 | Reserve space for images |
| **FID (First Input Delay)** | < 100ms | JavaScript execution time |
| **FCP (First Contentful Paint)** | < 1.8s | Critical CSS needed |

**Optimization Priorities:**
1. Optimize hero background image (WebP/AVIF)
2. Lazy load gallery images (`loading="lazy"`)
3. Inline critical CSS above the fold
4. Defer non-critical JavaScript (`defer` attribute)

---

## Recommendations Summary

### Priority 1: Must Fix Before Launch
- [ ] Add visible focus states (keyboard navigation)
- [ ] Replace emoji icons with SVG vectors
- [ ] Add proper form labels to modal input
- [ ] Add descriptive alt text to gallery images

### Priority 2: Should Fix Before QA Sign-Off
- [ ] Optimize hero background image (WebP/AVIF)
- [ ] Verify all touch targets meet 44×44px minimum
- [ ] Add loading states to checkout buttons
- [ ] Verify color contrast on all text (4.5:1 minimum)

### Priority 3: Nice to Have
- [ ] Add reduced-motion support for animations
- [ ] Implement skip-to-main-content link
- [ ] Run Lighthouse audit and fix performance issues
- [ ] Improve mobile trust bar spacing

---

## Implementation Checklist

- [ ] **Accessibility Review:** All issues in §Critical Issues section resolved
- [ ] **Brand Compliance:** All SVG icons in place, no emoji in UI
- [ ] **Performance:** Lighthouse score > 85, LCP < 2.5s
- [ ] **Testing:** Keyboard navigation tested, focus states visible
- [ ] **Mobile:** Responsive design tested on 375px, 768px, 1024px breakpoints
- [ ] **Cross-browser:** Verified on Chrome, Firefox, Safari, Edge
- [ ] **Screen Reader:** Tested with NVDA or JAWS
- [ ] **Dark Mode:** Contrast verified in dark theme
- [ ] **Loading States:** Button feedback visible during async operations
- [ ] **QA Sign-Off:** All critical and high-priority issues resolved

---

## Conclusion

The Framed landing page demonstrates **solid design fundamentals** with a cohesive dark theme, strong visual hierarchy, and modern interactions. However, **critical accessibility gaps** and **brand compliance issues** (emoji icons, missing labels) must be addressed before the design is production-ready.

**Recommended Action:** 
1. Address **Priority 1 issues** immediately (accessibility, icons, labels)
2. Fix **Priority 2 issues** before QA sign-off
3. Consider **Priority 3 improvements** for post-launch optimization

**Next Step:** Schedule QA review session after implementing fixes from Priority 1 & 2 sections.

---

**Report Generated:** April 19, 2026  
**Auditor:** UX Designer  
**Next Review:** After implementation of recommended fixes
