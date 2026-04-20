"""
QA Visual Screenshot Test for heyframed.com landing page (index.html)
Captures full-page screenshots of both index.html and the reference file.
Also evaluates which .reveal elements are actually visible vs hidden.
"""
from playwright.sync_api import sync_playwright
import json, os

BASE = r"E:\paperclip\_HEYFRAMED"

def test_page(page, file_path, label):
    url = f"file:///{file_path.replace(os.sep, '/')}"
    page.goto(url)
    page.wait_for_load_state('networkidle')
    # Wait a bit for fonts/images
    page.wait_for_timeout(2000)

    # Force-reveal all elements to check content presence
    page.evaluate("""
        document.querySelectorAll('.reveal').forEach(el => {
            el.classList.add('visible');
        });
    """)
    page.wait_for_timeout(500)

    # Take full-page screenshot (with reveals forced visible)
    screenshot_path = os.path.join(BASE, f"qa_{label}_forced_visible.png")
    page.screenshot(path=screenshot_path, full_page=True)
    print(f"[{label}] Saved forced-visible screenshot: {screenshot_path}")

    # Now reload and check WITHOUT forcing reveals (simulates real user view at page load)
    page.reload()
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(1000)
    # Don't scroll — check initial viewport only
    screenshot_initial = os.path.join(BASE, f"qa_{label}_initial_viewport.png")
    page.screenshot(path=screenshot_initial)
    print(f"[{label}] Saved initial viewport screenshot: {screenshot_initial}")

    # Check which sections have .reveal class and their visibility
    sections = page.evaluate("""
        () => {
            const results = [];
            document.querySelectorAll('.reveal').forEach((el, i) => {
                const rect = el.getBoundingClientRect();
                const style = window.getComputedStyle(el);
                const hasVisible = el.classList.contains('visible');
                // Try to get a meaningful label
                const heading = el.querySelector('h1,h2,h3,.section-label,.section-title,.step-num') ;
                const label = heading ? heading.textContent.trim().slice(0, 60) : (el.className || 'element-' + i);
                results.push({
                    index: i,
                    label: label,
                    hasVisible: hasVisible,
                    opacity: style.opacity,
                    inViewport: rect.top < window.innerHeight && rect.bottom > 0,
                    top: Math.round(rect.top),
                    height: Math.round(rect.height)
                });
            });
            return results;
        }
    """)

    print(f"\n[{label}] Reveal element analysis ({len(sections)} elements):")
    hidden = []
    for s in sections:
        status = "VISIBLE" if s['hasVisible'] else "HIDDEN"
        if not s['hasVisible']:
            hidden.append(s['label'])
        print(f"  [{status}] opacity={s['opacity']} inViewport={s['inViewport']} top={s['top']}px | {s['label']}")

    if hidden:
        print(f"\n[{label}] WARNING: {len(hidden)} elements start HIDDEN (opacity:0, no .visible class):")
        for h in hidden:
            print(f"  - {h}")
    else:
        print(f"\n[{label}] All reveal elements are visible on page load.")

    # Check which major sections exist in HTML
    sections_present = page.evaluate("""
        () => {
            const checks = {
                'nav': !!document.querySelector('nav.nav'),
                'hero': !!document.querySelector('#hero'),
                'trust-bar': !!document.querySelector('.trust-bar'),
                'how-it-works': !!document.querySelector('#how'),
                'gallery': !!document.querySelector('#gallery'),
                'categories': !!document.querySelector('#categories'),
                'pricing': !!document.querySelector('#pricing'),
                'final-cta': !!document.querySelector('.final-cta'),
                'footer': !!document.querySelector('footer'),
                'faq': !!document.querySelector('#faq'),
            };
            return checks;
        }
    """)

    print(f"\n[{label}] Section presence check:")
    for section, present in sections_present.items():
        status = "PRESENT" if present else "MISSING"
        print(f"  [{status}] {section}")

    return hidden, sections_present


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    # Test index.html
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    index_path = os.path.join(BASE, "index.html")
    ref_path = os.path.join(BASE, "Reference", "framed-landing-v3.html")
    
    print("=" * 60)
    print("TESTING: index.html (current landing page)")
    print("=" * 60)
    hidden_index, sections_index = test_page(page, index_path, "index")
    
    print("\n" + "=" * 60)
    print("TESTING: framed-landing-v3.html (reference)")
    print("=" * 60)
    hidden_ref, sections_ref = test_page(page, ref_path, "reference")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    # Check for missing sections
    missing_in_index = [k for k, v in sections_index.items() if not v]
    missing_in_ref = [k for k, v in sections_ref.items() if not v]
    present_in_ref_not_index = [k for k in sections_ref if sections_ref[k] and not sections_index.get(k, False)]
    
    print(f"\nSections PRESENT in reference but MISSING in index.html:")
    if present_in_ref_not_index:
        for s in present_in_ref_not_index:
            print(f"  MISSING: {s}")
    else:
        print("  None — all reference sections present in index.html")
    
    print(f"\nSections MISSING in index.html:")
    if missing_in_index:
        for s in missing_in_index:
            print(f"  MISSING: {s}")
    else:
        print("  None")
    
    print(f"\nHidden reveal elements on page load in index.html: {len(hidden_index)}")
    print(f"Hidden reveal elements on page load in reference: {len(hidden_ref)}")
    
    if hidden_index:
        print("\nCRITICAL: These sections start invisible due to .reveal animation (opacity:0):")
        for h in hidden_index:
            print(f"  - {h}")
    
    browser.close()
    print("\nDone. Screenshots saved to E:\\paperclip\\_HEYFRAMED\\")
