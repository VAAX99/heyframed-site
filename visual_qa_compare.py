#!/usr/bin/env python3
"""
Visual QA Comparison Script: Live vs Reference
Compares live heyframed.com index.html against reference design
Generates side-by-side screenshots for manual review
"""

from playwright.sync_api import sync_playwright
import os
import time

# Configuration
CURRENT_FILE = "E:\\paperclip\\_HEYFRAMED\\index.html"
REFERENCE_FILE = "E:\\paperclip\\_HEYFRAMED\\Reference\\framed-landing-v3.html"
OUTPUT_DIR = "E:\\paperclip\\_HEYFRAMED"

# Breakpoints to test
BREAKPOINTS = {
    "desktop": (1440, 900),
    "tablet": (768, 1024),
    "mobile": (375, 667),
}

def take_screenshots():
    """Take screenshots of current and reference at all breakpoints"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # Test current index.html
        print("[QA] Testing current index.html...")
        page_current = browser.new_page()
        page_current.goto(f"file:///{CURRENT_FILE.replace(chr(92), '/')}")
        page_current.wait_for_load_state("networkidle")
        
        # Test reference design
        print("[QA] Testing reference design...")
        page_ref = browser.new_page()
        page_ref.goto(f"file:///{REFERENCE_FILE.replace(chr(92), '/')}")
        page_ref.wait_for_load_state("networkidle")
        
        # Take screenshots at each breakpoint
        for breakpoint_name, (width, height) in BREAKPOINTS.items():
            print(f"[QA] Capturing {breakpoint_name} ({width}x{height})...")
            
            # Current
            page_current.set_viewport_size({"width": width, "height": height})
            time.sleep(0.5)  # Allow re-layout
            screenshot_current = os.path.join(OUTPUT_DIR, f"qa_visual_current_{breakpoint_name}.png")
            page_current.screenshot(path=screenshot_current, full_page=True)
            print(f"  ✓ Saved: {screenshot_current}")
            
            # Reference
            page_ref.set_viewport_size({"width": width, "height": height})
            time.sleep(0.5)
            screenshot_ref = os.path.join(OUTPUT_DIR, f"qa_visual_reference_{breakpoint_name}.png")
            page_ref.screenshot(path=screenshot_ref, full_page=True)
            print(f"  ✓ Saved: {screenshot_ref}")
        
        # Also test section-by-section for detailed comparison
        print("[QA] Capturing section details...")
        
        # Hero section
        page_current.set_viewport_size({"width": 1440, "height": 900})
        hero_current = os.path.join(OUTPUT_DIR, f"qa_visual_current_hero_detail.png")
        page_current.locator(".hero").screenshot(path=hero_current)
        
        hero_ref = os.path.join(OUTPUT_DIR, f"qa_visual_reference_hero_detail.png")
        page_ref.set_viewport_size({"width": 1440, "height": 900})
        page_ref.locator(".hero").screenshot(path=hero_ref)
        
        # Trust bar
        trust_current = os.path.join(OUTPUT_DIR, f"qa_visual_current_trust_detail.png")
        page_current.locator(".trust-bar").screenshot(path=trust_current)
        
        trust_ref = os.path.join(OUTPUT_DIR, f"qa_visual_reference_trust_detail.png")
        page_ref.locator(".trust-bar").screenshot(path=trust_ref)
        
        # Pricing section
        page_current.goto(f"file:///{CURRENT_FILE.replace(chr(92), '/')}")
        page_current.wait_for_load_state("networkidle")
        page_current.locator("#pricing").scroll_into_view()
        
        page_ref.goto(f"file:///{REFERENCE_FILE.replace(chr(92), '/')}")
        page_ref.wait_for_load_state("networkidle")
        page_ref.locator("#pricing").scroll_into_view()
        
        pricing_current = os.path.join(OUTPUT_DIR, f"qa_visual_current_pricing_detail.png")
        page_current.locator("#pricing").screenshot(path=pricing_current)
        
        pricing_ref = os.path.join(OUTPUT_DIR, f"qa_visual_reference_pricing_detail.png")
        page_ref.locator("#pricing").screenshot(path=pricing_ref)
        
        browser.close()
        
        print("\n[QA] ✓ All screenshots captured successfully!")
        print("[QA] Check output directory for comparison files")

def check_accessibility():
    """Run basic accessibility checks"""
    print("\n[QA] Running accessibility checks...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file:///{CURRENT_FILE.replace(chr(92), '/')}")
        page.wait_for_load_state("networkidle")
        
        # Check for focus-visible support
        focus_result = page.evaluate("() => window.getComputedStyle(document.querySelector('button:focus-visible')).outlineWidth")
        
        # Check for ARIA labels
        buttons_without_label = page.evaluate("""() => {
            const buttons = Array.from(document.querySelectorAll('button'));
            return buttons.filter(b => !b.getAttribute('aria-label') && !b.textContent.trim()).length;
        }""")
        
        # Check for images with alt text
        images = page.evaluate("""() => {
            const imgs = Array.from(document.querySelectorAll('img'));
            return {
                total: imgs.length,
                withAlt: imgs.filter(i => i.getAttribute('alt')).length,
                withoutAlt: imgs.filter(i => !i.getAttribute('alt')).length,
            };
        }""")
        
        print(f"  • Images: {images['total']} total, {images['withAlt']} with alt, {images['withoutAlt']} without alt")
        print(f"  • Buttons without ARIA labels: {buttons_without_label}")
        
        browser.close()

if __name__ == "__main__":
    print("=" * 60)
    print("FRAMED LANDING PAGE - VISUAL QA COMPARISON")
    print("=" * 60)
    
    # Verify files exist
    if not os.path.exists(CURRENT_FILE):
        print(f"❌ Error: Current file not found: {CURRENT_FILE}")
        exit(1)
    
    if not os.path.exists(REFERENCE_FILE):
        print(f"❌ Error: Reference file not found: {REFERENCE_FILE}")
        exit(1)
    
    print(f"Current file: {CURRENT_FILE}")
    print(f"Reference file: {REFERENCE_FILE}")
    print()
    
    # Take screenshots
    take_screenshots()
    
    # Run accessibility checks
    check_accessibility()
    
    print("\n" + "=" * 60)
    print("VISUAL QA COMPLETE")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review generated screenshots in output directory")
    print("2. Compare visual hierarchy, spacing, and typography")
    print("3. Verify responsive behavior across breakpoints")
    print("4. Check accessibility compliance")
    print("5. Document any discrepancies for fixes")
