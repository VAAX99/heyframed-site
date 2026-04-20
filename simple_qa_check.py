#!/usr/bin/env python3
"""
Simple QA validation for Framed Landing Page
Focuses on key verification points without complex Unicode output
"""

from playwright.sync_api import sync_playwright
import time

def validate_landing_page():
    """Validate current landing page against requirements"""
    
    issues = []
    passes = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Loading current index.html...")
        page.goto('file:///E:/paperclip/_HEYFRAMED/index.html')
        page.wait_for_load_state('networkidle')
        
        # Take screenshots
        page.screenshot(path='E:/paperclip/_HEYFRAMED/qa_current_desktop.png', full_page=True)
        
        # Check brand compliance
        print("Checking brand compliance...")
        
        # 1. Check accent color
        try:
            accent_color = page.evaluate("() => getComputedStyle(document.documentElement).getPropertyValue('--accent').trim()")
            if accent_color.upper() == '#F0B429':
                passes.append("Brand accent color correct: #F0B429")
            else:
                issues.append(f"Brand accent color wrong: {accent_color}, expected #F0B429")
        except:
            issues.append("Could not check accent color")
        
        # 2. Check typography (Inter font)
        try:
            font_family = page.evaluate("() => getComputedStyle(document.body).fontFamily")
            if 'Inter' in font_family:
                passes.append("Inter font family correctly applied")
            else:
                issues.append(f"Wrong font family: {font_family}")
        except:
            issues.append("Could not check font family")
        
        # 3. Check logo format
        try:
            logo_html = page.locator('.nav-logo').inner_html()
            if 'FRAME' in logo_html and '<span' in logo_html and 'D</span>' in logo_html:
                passes.append("Logo format correct (FRAMED with accent D)")
            else:
                issues.append(f"Logo format incorrect: {logo_html}")
        except:
            issues.append("Could not check logo format")
        
        # 4. Check tagline in hero
        try:
            hero_text = page.locator('.hero-h1').inner_text()
            if 'framed' in hero_text.lower() and 'story' in hero_text.lower():
                passes.append("Brand tagline elements present in hero")
            else:
                issues.append(f"Brand tagline missing elements: {hero_text}")
        except:
            issues.append("Could not check hero tagline")
        
        # 5. Check Telegram links
        print("Checking Telegram links...")
        try:
            telegram_links = page.locator('a[href="#telegram"]').count()
            if telegram_links >= 3:
                passes.append(f"Telegram links present: {telegram_links} found")
            else:
                issues.append(f"Insufficient Telegram links: {telegram_links} found, expected >=3")
        except:
            issues.append("Could not check Telegram links")
        
        # 6. Check analytics
        print("Checking analytics...")
        try:
            plausible_script = page.locator('script[src*="plausible.io"]').count()
            csp_meta = page.locator('meta[http-equiv="Content-Security-Policy"]').count()
            
            if plausible_script > 0:
                passes.append("Plausible analytics script present")
            else:
                issues.append("Plausible analytics script missing")
                
            if csp_meta > 0:
                passes.append("CSP security header present")
            else:
                issues.append("CSP security header missing")
        except:
            issues.append("Could not check analytics")
        
        # 7. Test checkout modal
        print("Testing checkout flow...")
        try:
            page.locator('button[onclick*="openCheckout"]').first.click()
            time.sleep(1)
            
            modal_visible = page.locator('#checkoutModal.open').is_visible()
            if modal_visible:
                passes.append("Checkout modal opens correctly")
                
                # Check modal elements
                if page.locator('#chatIdInput').is_visible():
                    passes.append("Chat ID input field present")
                else:
                    issues.append("Chat ID input field missing")
                    
                # Close modal
                page.locator('.modal-close').click()
                time.sleep(1)
            else:
                issues.append("Checkout modal does not open")
        except Exception as e:
            issues.append(f"Checkout flow error: {str(e)}")
        
        # 8. Test responsive design
        print("Testing responsive design...")
        try:
            # Mobile test
            page.set_viewport_size({'width': 375, 'height': 812})
            page.wait_for_timeout(1000)
            page.screenshot(path='E:/paperclip/_HEYFRAMED/qa_current_mobile.png', full_page=True)
            
            nav_visible = page.locator('.nav').is_visible()
            hero_visible = page.locator('.hero').is_visible()
            
            if nav_visible and hero_visible:
                passes.append("Mobile layout renders correctly")
            else:
                issues.append("Mobile layout has visibility issues")
                
        except Exception as e:
            issues.append(f"Responsive test error: {str(e)}")
        
        browser.close()
    
    return issues, passes

def compare_with_reference():
    """Compare key elements with reference design"""
    
    comparison_issues = []
    comparison_passes = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        
        # Load both pages
        current = context.new_page()
        reference = context.new_page()
        
        current.goto('file:///E:/paperclip/_HEYFRAMED/index.html')
        reference.goto('file:///E:/paperclip/_HEYFRAMED/Reference/framed-landing-v3.html')
        
        current.wait_for_load_state('networkidle')
        reference.wait_for_load_state('networkidle')
        
        # Compare sections
        try:
            current_sections = current.locator('section').count()
            ref_sections = reference.locator('section').count()
            
            if current_sections == ref_sections:
                comparison_passes.append(f"Section count matches: {current_sections}")
            else:
                comparison_issues.append(f"Section count differs: current({current_sections}) vs reference({ref_sections})")
        except:
            comparison_issues.append("Could not compare sections")
        
        # Compare pricing
        try:
            current_prices = current.locator('.price-amount').count()
            ref_prices = reference.locator('.price-amount').count()
            
            if current_prices == ref_prices:
                comparison_passes.append(f"Pricing tiers match: {current_prices}")
            else:
                comparison_issues.append(f"Pricing tiers differ: current({current_prices}) vs reference({ref_prices})")
        except:
            comparison_issues.append("Could not compare pricing")
        
        # Compare navigation
        try:
            current_nav = current.locator('.nav-logo').inner_text()
            ref_nav = reference.locator('.nav-logo').inner_text()
            
            if current_nav == ref_nav:
                comparison_passes.append("Navigation logo matches")
            else:
                comparison_issues.append(f"Navigation differs: '{current_nav}' vs '{ref_nav}'")
        except:
            comparison_issues.append("Could not compare navigation")
        
        browser.close()
    
    return comparison_issues, comparison_passes

if __name__ == "__main__":
    print("== FRAMED LANDING PAGE QA VALIDATION ==")
    print("Checking current implementation against requirements...")
    print()
    
    # Run main validation
    issues, passes = validate_landing_page()
    
    print("Comparing with reference design...")
    comparison_issues, comparison_passes = compare_with_reference()
    
    # Combine results
    all_issues = issues + comparison_issues
    all_passes = passes + comparison_passes
    
    print("\n" + "="*60)
    print("QA VALIDATION RESULTS")
    print("="*60)
    
    print(f"\nPASSED CHECKS ({len(all_passes)}):")
    for i, check in enumerate(all_passes, 1):
        print(f"  {i}. {check}")
    
    print(f"\nISSUES FOUND ({len(all_issues)}):")
    if all_issues:
        for i, issue in enumerate(all_issues, 1):
            print(f"  {i}. {issue}")
    else:
        print("  No issues found!")
    
    print(f"\nSUMMARY:")
    print(f"  Total checks: {len(all_passes) + len(all_issues)}")
    print(f"  Passed: {len(all_passes)}")
    print(f"  Failed: {len(all_issues)}")
    
    pass_rate = (len(all_passes) / (len(all_passes) + len(all_issues))) * 100 if (len(all_passes) + len(all_issues)) > 0 else 0
    print(f"  Pass rate: {pass_rate:.1f}%")
    
    if len(all_issues) == 0:
        print("\n✓ STATUS: READY FOR PRODUCTION")
        print("  Landing page matches reference design and brand guidelines.")
    elif len(all_issues) <= 2:
        print("\n⚠ STATUS: MINOR ISSUES - REVIEW RECOMMENDED") 
        print("  Most checks passed but some issues need attention.")
    else:
        print("\n✗ STATUS: MAJOR ISSUES - FIXES REQUIRED")
        print("  Multiple issues found that need to be addressed.")
    
    print(f"\nScreenshots saved:")
    print(f"  - qa_current_desktop.png (Full desktop view)")
    print(f"  - qa_current_mobile.png (Mobile responsive view)")
    print()