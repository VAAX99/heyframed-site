"""
QA Scroll Test: verify IntersectionObserver works in headless browser
by scrolling through the page and confirming sections become visible.
Also check CSP impact.
"""
from playwright.sync_api import sync_playwright
import os

BASE = r"E:\paperclip\_HEYFRAMED"

def scroll_and_check(page, file_path, label):
    url = f"file:///{file_path.replace(os.sep, '/')}"
    
    # Capture console errors
    errors = []
    page.on("console", lambda msg: errors.append(f"[{msg.type}] {msg.text}") if msg.type in ("error", "warning") else None)
    page.on("pageerror", lambda err: errors.append(f"[pageerror] {err}"))
    
    page.goto(url)
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(1500)
    
    # Take screenshot at top
    page.screenshot(path=os.path.join(BASE, f"qa_{label}_scroll_top.png"))
    
    # Scroll to bottom slowly (in increments)
    page.evaluate("""
        async () => {
            const delay = ms => new Promise(res => setTimeout(res, ms));
            const totalHeight = document.body.scrollHeight;
            const step = 300;
            for (let y = 0; y < totalHeight; y += step) {
                window.scrollTo(0, y);
                await delay(120);
            }
            window.scrollTo(0, totalHeight);
            await delay(500);
        }
    """)
    page.wait_for_timeout(1000)
    
    # Screenshot at bottom
    page.screenshot(path=os.path.join(BASE, f"qa_{label}_scroll_bottom.png"), full_page=True)
    
    # Check how many are now visible
    visible_count = page.evaluate("""
        () => document.querySelectorAll('.reveal.visible').length
    """)
    total_count = page.evaluate("""
        () => document.querySelectorAll('.reveal').length
    """)
    still_hidden = page.evaluate("""
        () => {
            const hidden = [];
            document.querySelectorAll('.reveal:not(.visible)').forEach(el => {
                const h = el.querySelector('h1,h2,h3,.section-label,.section-title,.step-num');
                hidden.push(h ? h.textContent.trim().slice(0, 60) : el.className.slice(0, 60));
            });
            return hidden;
        }
    """)
    
    print(f"\n[{label}] After full scroll: {visible_count}/{total_count} reveal elements now visible")
    if still_hidden:
        print(f"  Still hidden: {still_hidden}")
    
    if errors:
        print(f"\n[{label}] Console errors/warnings:")
        for e in errors:
            print(f"  {e}")
    else:
        print(f"\n[{label}] No console errors.")
    
    return visible_count, total_count

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    
    index_path = os.path.join(BASE, "index.html")
    ref_path = os.path.join(BASE, "Reference", "framed-landing-v3.html")
    
    print("=" * 60)
    print("SCROLL TEST: index.html")
    print("=" * 60)
    v_index, t_index = scroll_and_check(page, index_path, "index")
    
    print("\n" + "=" * 60)
    print("SCROLL TEST: reference")
    print("=" * 60)
    v_ref, t_ref = scroll_and_check(page, ref_path, "reference")
    
    print("\n" + "=" * 60)
    print("SCROLL SUMMARY")
    print("=" * 60)
    print(f"index.html:  {v_index}/{t_index} elements become visible on scroll")
    print(f"reference:   {v_ref}/{t_ref} elements become visible on scroll")
    
    if v_index < t_index:
        print(f"\nFAIL: {t_index - v_index} elements NEVER become visible in index.html even after full scroll!")
    else:
        print("\nPASS: All elements in index.html become visible after scrolling.")
    
    if v_ref < t_ref:
        print(f"FAIL: {t_ref - v_ref} elements NEVER become visible in reference even after full scroll!")
    else:
        print("PASS: All elements in reference become visible after scrolling.")
    
    browser.close()
