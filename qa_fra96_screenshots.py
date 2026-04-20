"""
FRA-96 Screenshot evidence: capture key sections showing visibility
"""
from playwright.sync_api import sync_playwright
import os

BASE = r"E:\paperclip\_HEYFRAMED"
INDEX = os.path.join(BASE, "index.html")
INDEX_URL = f"file:///{INDEX.replace(os.sep, '/')}"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    # ── Desktop initial viewport ───────────────────────────────────────────────
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(INDEX_URL)
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1200)

    # 1. Hero visible on load
    page.screenshot(path=os.path.join(BASE, "qa_fra96_01_hero_initial.png"))
    print("Screenshot 1: Hero initial viewport")

    # 2. Full page BEFORE any scrolling (shows below-fold is present in DOM, opacity:0 for below-fold only)
    page.screenshot(path=os.path.join(BASE, "qa_fra96_02_full_before_scroll.png"), full_page=True)
    print("Screenshot 2: Full page before scroll")

    # Scroll to How It Works section
    page.evaluate("document.querySelector('#how-it-works, section:nth-of-type(2), .section-how, [data-section=\"how\"]') && document.querySelector('#how-it-works, section:nth-of-type(2), .section-how, [data-section=\"how\"]').scrollIntoView({behavior:'instant'})")
    page.wait_for_timeout(800)
    page.screenshot(path=os.path.join(BASE, "qa_fra96_03_how_it_works.png"))
    print("Screenshot 3: How It Works section")

    # Scroll to bottom slowly
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

    # 3. Full page AFTER scrolling (all sections should now be visible/revealed)
    page.screenshot(path=os.path.join(BASE, "qa_fra96_04_full_after_scroll.png"), full_page=True)
    print("Screenshot 4: Full page after scroll (all sections revealed)")

    # Verify all visible
    visible = page.evaluate("() => document.querySelectorAll('.reveal.visible').length")
    total = page.evaluate("() => document.querySelectorAll('.reveal').length")
    print(f"  .reveal.visible: {visible}/{total}")

    page.close()

    # ── No-JS screenshot (verify no opacity:0 without JS) ─────────────────────
    page_nojs = browser.new_page(viewport={"width": 1440, "height": 900}, java_script_enabled=False)
    page_nojs.goto(INDEX_URL)
    page_nojs.wait_for_load_state("domcontentloaded")
    page_nojs.wait_for_timeout(600)
    page_nojs.screenshot(path=os.path.join(BASE, "qa_fra96_05_nojs_full.png"), full_page=True)
    print("Screenshot 5: No-JS full page (all content should be visible)")
    page_nojs.close()

    # ── Mobile viewport ────────────────────────────────────────────────────────
    page_mob = browser.new_page(viewport={"width": 390, "height": 844})
    page_mob.goto(INDEX_URL)
    page_mob.wait_for_load_state("networkidle")
    page_mob.wait_for_timeout(1000)
    page_mob.screenshot(path=os.path.join(BASE, "qa_fra96_06_mobile_initial.png"))
    print("Screenshot 6: Mobile initial viewport")

    page_mob.evaluate("""
        async () => {
            const delay = ms => new Promise(r => setTimeout(r, ms));
            const h = document.body.scrollHeight;
            for (let y = 0; y < h; y += 200) {
                window.scrollTo(0, y);
                await delay(130);
            }
            window.scrollTo(0, h);
        }
    """)
    page_mob.wait_for_timeout(800)
    page_mob.screenshot(path=os.path.join(BASE, "qa_fra96_07_mobile_after_scroll.png"), full_page=True)
    print("Screenshot 7: Mobile full page after scroll")
    page_mob.close()

    browser.close()
    print("\nAll screenshots captured.")
