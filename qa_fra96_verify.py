"""
FRA-96 QA Verification: reveal animation fix
Tests:
1. Below-fold content visible on initial page load (no JS → no opacity:0)
2. With JS active: elements start hidden, become visible on scroll
3. No layout shifts or FOIC
"""
from playwright.sync_api import sync_playwright
import os, json

BASE = r"E:\paperclip\_HEYFRAMED"
INDEX = os.path.join(BASE, "index.html")
INDEX_URL = f"file:///{INDEX.replace(os.sep, '/')}"

SECTIONS = ["How It Works", "Gallery", "Categories", "Pricing", "Final CTA"]
RESULTS = {}

def run_tests():
    with sync_playwright() as p:
        # ── Test 1: JS DISABLED – all reveal content must be visible ─────────────
        print("\n" + "="*60)
        print("TEST 1: JS disabled (simulate no-JS environment)")
        print("="*60)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900}, java_script_enabled=False)
        page.goto(INDEX_URL)
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(800)

        # Full-page screenshot without JS
        page.screenshot(path=os.path.join(BASE, "qa_fra96_nojs_full.png"), full_page=True)

        # Check: no js-enabled class on <html>
        has_js_class = page.evaluate("() => document.documentElement.classList.contains('js-enabled')")
        print(f"  html.js-enabled present without JS: {has_js_class} (expected: False)")

        # Check: .reveal elements should NOT be opacity:0 without js-enabled
        hidden_count = page.evaluate("""
            () => {
                const els = document.querySelectorAll('.reveal');
                let hiddenCount = 0;
                els.forEach(el => {
                    const style = window.getComputedStyle(el);
                    if (parseFloat(style.opacity) < 0.5) hiddenCount++;
                });
                return hiddenCount;
            }
        """)
        total_reveal = page.evaluate("() => document.querySelectorAll('.reveal').length")
        print(f"  Hidden .reveal elements (opacity<0.5) without JS: {hidden_count}/{total_reveal} (expected: 0/N)")

        RESULTS["test1_js_class_without_js"] = not has_js_class
        RESULTS["test1_no_hidden_elements"] = hidden_count == 0
        RESULTS["test1_total_reveal"] = total_reveal

        browser.close()

        # ── Test 2: JS ENABLED – initial viewport check ───────────────────────────
        print("\n" + "="*60)
        print("TEST 2: JS enabled – initial load (no scroll)")
        print("="*60)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})

        console_errors = []
        page.on("console", lambda m: console_errors.append(f"[{m.type}] {m.text}") if m.type in ("error","warning") else None)
        page.on("pageerror", lambda e: console_errors.append(f"[pageerror] {e}"))

        page.goto(INDEX_URL)
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1200)

        # Screenshot at initial viewport (no scroll)
        page.screenshot(path=os.path.join(BASE, "qa_fra96_js_initial.png"))

        # Confirm js-enabled is set
        has_js = page.evaluate("() => document.documentElement.classList.contains('js-enabled')")
        print(f"  html.js-enabled present with JS: {has_js} (expected: True)")

        # Check how many reveal elements are in viewport (should be visible)
        in_viewport_visible = page.evaluate("""
            () => {
                const vw = window.innerWidth, vh = window.innerHeight;
                let visibleInViewport = 0, hiddenInViewport = 0;
                document.querySelectorAll('.reveal').forEach(el => {
                    const rect = el.getBoundingClientRect();
                    const inViewport = rect.top < vh && rect.bottom > 0;
                    if (inViewport) {
                        const style = window.getComputedStyle(el);
                        const visible = parseFloat(style.opacity) > 0.5;
                        if (visible) visibleInViewport++;
                        else hiddenInViewport++;
                    }
                });
                return { visibleInViewport, hiddenInViewport };
            }
        """)
        print(f"  In-viewport reveal elements: {in_viewport_visible['visibleInViewport']} visible, {in_viewport_visible['hiddenInViewport']} hidden (expected: hidden=0 if hero is in viewport)")

        # Count out-of-viewport (below-fold) elements with opacity:0
        below_fold_hidden = page.evaluate("""
            () => {
                const vh = window.innerHeight;
                let count = 0;
                document.querySelectorAll('.reveal').forEach(el => {
                    const rect = el.getBoundingClientRect();
                    const belowFold = rect.top >= vh;
                    if (belowFold) {
                        const style = window.getComputedStyle(el);
                        if (parseFloat(style.opacity) < 0.5) count++;
                    }
                });
                return count;
            }
        """)
        total_below = page.evaluate("""
            () => {
                const vh = window.innerHeight;
                let count = 0;
                document.querySelectorAll('.reveal').forEach(el => {
                    const rect = el.getBoundingClientRect();
                    if (rect.top >= vh) count++;
                });
                return count;
            }
        """)
        print(f"  Below-fold reveal elements hidden (opacity:0): {below_fold_hidden}/{total_below}")
        print(f"  NOTE: Below-fold CAN legitimately be hidden by JS (waiting for scroll reveal)")
        
        RESULTS["test2_js_enabled"] = has_js
        RESULTS["test2_in_viewport_visible"] = in_viewport_visible

        # ── Test 3: SCROLL – all elements become visible ──────────────────────────
        print("\n" + "="*60)
        print("TEST 3: Scroll through full page – all elements should become visible")
        print("="*60)

        # Take screenshot at initial full page to see all sections
        page.screenshot(path=os.path.join(BASE, "qa_fra96_js_initial_full.png"), full_page=True)

        page.evaluate("""
            async () => {
                const delay = ms => new Promise(r => setTimeout(r, ms));
                const h = document.body.scrollHeight;
                for (let y = 0; y < h; y += 250) {
                    window.scrollTo(0, y);
                    await delay(150);
                }
                window.scrollTo(0, h);
                await delay(600);
            }
        """)
        page.wait_for_timeout(1000)

        page.screenshot(path=os.path.join(BASE, "qa_fra96_after_scroll.png"), full_page=True)

        visible_after = page.evaluate("() => document.querySelectorAll('.reveal.visible').length")
        total_reveal_js = page.evaluate("() => document.querySelectorAll('.reveal').length")
        still_hidden = page.evaluate("""
            () => {
                const out = [];
                document.querySelectorAll('.reveal:not(.visible)').forEach(el => {
                    const h = el.querySelector('h1,h2,h3,.section-label,.section-title,.step-num,.section-header');
                    out.push(h ? h.textContent.trim().slice(0,60) : el.className.slice(0,60));
                });
                return out;
            }
        """)

        print(f"  After scroll: {visible_after}/{total_reveal_js} reveal elements have .visible class")
        if still_hidden:
            print(f"  STILL HIDDEN: {still_hidden}")
        else:
            print(f"  All reveal elements received .visible class")

        RESULTS["test3_visible_after_scroll"] = visible_after
        RESULTS["test3_total"] = total_reveal_js
        RESULTS["test3_still_hidden"] = still_hidden
        RESULTS["test3_all_visible"] = visible_after == total_reveal_js

        # ── Test 4: MOBILE – repeat initial check on mobile viewport ─────────────
        print("\n" + "="*60)
        print("TEST 4: Mobile viewport (390x844 – iPhone 14)")
        print("="*60)
        page2 = browser.new_page(viewport={"width": 390, "height": 844})
        page2.goto(INDEX_URL)
        page2.wait_for_load_state("networkidle")
        page2.wait_for_timeout(1000)
        page2.screenshot(path=os.path.join(BASE, "qa_fra96_mobile_initial.png"))

        mobile_hidden = page2.evaluate("""
            () => {
                const els = document.querySelectorAll('.reveal');
                let h = 0;
                els.forEach(el => {
                    const s = window.getComputedStyle(el);
                    if (parseFloat(s.opacity) < 0.5) h++;
                });
                return h;
            }
        """)
        mobile_total = page2.evaluate("() => document.querySelectorAll('.reveal').length")
        print(f"  Mobile: {mobile_hidden}/{mobile_total} reveal elements hidden on load (these are below-fold – OK if JS handles them)")

        page2.evaluate("""
            async () => {
                const delay = ms => new Promise(r => setTimeout(r, ms));
                const h = document.body.scrollHeight;
                for (let y = 0; y < h; y += 200) {
                    window.scrollTo(0, y);
                    await delay(130);
                }
                window.scrollTo(0, h);
                await delay(500);
            }
        """)
        page2.wait_for_timeout(800)
        page2.screenshot(path=os.path.join(BASE, "qa_fra96_mobile_after_scroll.png"), full_page=True)

        mobile_visible = page2.evaluate("() => document.querySelectorAll('.reveal.visible').length")
        print(f"  Mobile after scroll: {mobile_visible}/{mobile_total} visible")
        RESULTS["test4_mobile_visible_after_scroll"] = mobile_visible == mobile_total

        page2.close()
        
        if console_errors:
            print(f"\nConsole errors detected:")
            for e in console_errors:
                print(f"  {e}")
        else:
            print("\nNo console errors.")

        RESULTS["console_errors"] = console_errors
        browser.close()

    # ── Summary ────────────────────────────────────────────────────────────────
    print("\n" + "="*60)
    print("FRA-96 QA SUMMARY")
    print("="*60)

    checks = [
        ("No hidden elements without JS (opacity:0 guard)", RESULTS.get("test1_no_hidden_elements")),
        ("js-enabled class absent when JS disabled", RESULTS.get("test1_js_class_without_js")),
        ("js-enabled class present when JS active", RESULTS.get("test2_js_enabled")),
        ("All reveal elements become visible after scroll", RESULTS.get("test3_all_visible")),
        ("Mobile: all elements visible after scroll", RESULTS.get("test4_mobile_visible_after_scroll")),
    ]

    passed = sum(1 for _, v in checks if v)
    total = len(checks)

    for label, result in checks:
        status = "PASS" if result else "FAIL"
        print(f"  [{status}] {label}")

    print(f"\nResult: {passed}/{total} checks passed")
    overall = passed == total
    print(f"OVERALL: {'PASS - FRA-96 fix confirmed' if overall else 'FAIL - issues remain'}")

    # Write results to file
    with open(os.path.join(BASE, "qa_fra96_results.txt"), "w") as f:
        f.write(f"FRA-96 QA Results\n{'='*60}\n\n")
        for label, result in checks:
            status = "PASS" if result else "FAIL"
            f.write(f"[{status}] {label}\n")
        f.write(f"\nResult: {passed}/{total} checks passed\n")
        f.write(f"OVERALL: {'PASS' if overall else 'FAIL'}\n\n")
        f.write(f"Details:\n{json.dumps(RESULTS, indent=2)}\n")

    return overall

if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
