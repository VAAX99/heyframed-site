#!/usr/bin/env python3
"""
QA Validation Script for Framed Landing Page
Compares current index.html with reference design and validates functionality
"""

from playwright.sync_api import sync_playwright
import time
import json
from pathlib import Path

def test_landing_page_comparison():
    """Compare current landing page with reference design"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        
        results = {
            'visual_comparison': {},
            'telegram_links': [],
            'checkout_flow': {},
            'analytics_check': {},
            'responsive_test': {},
            'issues_found': []
        }
        
        # Test current index.html
        print(">> Testing current index.html...")
        current_page = context.new_page()
        current_page.goto('file:///E:/paperclip/_HEYFRAMED/index.html')
        current_page.wait_for_load_state('networkidle')
        current_page.screenshot(path='E:/paperclip/_HEYFRAMED/qa_current_full.png', full_page=True)
        
        # Test reference design
        print(">> Testing reference framed-landing-v3.html...")
        ref_page = context.new_page()
        ref_page.goto('file:///E:/paperclip/_HEYFRAMED/Reference/framed-landing-v3.html')
        ref_page.wait_for_load_state('networkidle')
        ref_page.screenshot(path='E:/paperclip/_HEYFRAMED/qa_reference_full.png', full_page=True)
        
        # Visual comparison tests
        print(">> Performing visual comparison...")
        
        # Check page structure and sections
        current_sections = current_page.locator('section').count()
        ref_sections = ref_page.locator('section').count()
        
        results['visual_comparison']['sections_count'] = {
            'current': current_sections,
            'reference': ref_sections,
            'match': current_sections == ref_sections
        }
        
        # Check navigation
        current_nav = current_page.locator('.nav-logo').inner_text()
        ref_nav = ref_page.locator('.nav-logo').inner_text()
        
        results['visual_comparison']['navigation'] = {
            'current': current_nav,
            'reference': ref_nav,
            'match': current_nav == ref_nav
        }
        
        # Check hero section
        current_hero = current_page.locator('.hero-h1').inner_text()
        ref_hero = ref_page.locator('.hero-h1').inner_text()
        
        results['visual_comparison']['hero_title'] = {
            'current': current_hero.replace('\\n', ' ').strip(),
            'reference': ref_hero.replace('\\n', ' ').strip(),
            'match': current_hero.replace('\\n', ' ').strip() == ref_hero.replace('\\n', ' ').strip()
        }
        
        # Check pricing section
        current_prices = [elem.inner_text() for elem in current_page.locator('.price-amount').all()]
        ref_prices = [elem.inner_text() for elem in ref_page.locator('.price-amount').all()]
        
        results['visual_comparison']['pricing'] = {
            'current': current_prices,
            'reference': ref_prices,
            'match': current_prices == ref_prices
        }
        
        # Test Telegram links functionality
        print(">> Testing Telegram links...")
        telegram_links = current_page.locator('a[href="#telegram"]').all()
        
        for i, link in enumerate(telegram_links):
            link_text = link.inner_text()
            results['telegram_links'].append({
                'index': i + 1,
                'text': link_text,
                'href': link.get_attribute('href'),
                'visible': link.is_visible()
            })
        
        # Test checkout flow
        print(">> Testing checkout flow...")
        try:
            # Click a subscription button
            current_page.locator('button[onclick*="openCheckout"]').first.click()
            time.sleep(1)
            
            # Check if modal opens
            modal_visible = current_page.locator('#checkoutModal.open').is_visible()
            results['checkout_flow']['modal_opens'] = modal_visible
            
            if modal_visible:
                # Test modal elements
                results['checkout_flow']['modal_elements'] = {
                    'close_button': current_page.locator('.modal-close').is_visible(),
                    'chat_id_input': current_page.locator('#chatIdInput').is_visible(),
                    'continue_button': current_page.locator('.modal-cta').is_visible()
                }
                
                # Close modal
                current_page.locator('.modal-close').click()
                time.sleep(1)
                
        except Exception as e:
            results['checkout_flow']['error'] = str(e)
            results['issues_found'].append(f"Checkout flow error: {e}")
        
        # Check analytics implementation
        print(">> Checking analytics...")
        
        # Check if Plausible script is present
        plausible_script = current_page.locator('script[src*="plausible.io"]').count()
        csp_meta = current_page.locator('meta[http-equiv="Content-Security-Policy"]').count()
        
        results['analytics_check'] = {
            'plausible_script_present': plausible_script > 0,
            'csp_header_present': csp_meta > 0,
            'analytics_provider_meta': current_page.locator('meta[name="analytics-provider"]').count() > 0
        }
        
        # Test responsive behavior
        print(">> Testing responsive behavior...")
        
        # Test mobile viewport
        current_page.set_viewport_size({'width': 375, 'height': 812})
        current_page.wait_for_timeout(1000)
        current_page.screenshot(path='E:/paperclip/_HEYFRAMED/qa_current_mobile.png', full_page=True)
        
        # Check mobile navigation
        mobile_nav_visible = current_page.locator('.nav').is_visible()
        hero_visible = current_page.locator('.hero').is_visible()
        
        results['responsive_test']['mobile'] = {
            'navigation_visible': mobile_nav_visible,
            'hero_visible': hero_visible,
            'viewport': '375x812'
        }
        
        # Test tablet viewport
        current_page.set_viewport_size({'width': 768, 'height': 1024})
        current_page.wait_for_timeout(1000)
        current_page.screenshot(path='E:/paperclip/_HEYFRAMED/qa_current_tablet.png', full_page=True)
        
        results['responsive_test']['tablet'] = {
            'navigation_visible': current_page.locator('.nav').is_visible(),
            'hero_visible': current_page.locator('.hero').is_visible(),
            'viewport': '768x1024'
        }
        
        # Check for JavaScript errors
        current_page.on('console', lambda msg: results['issues_found'].append(f"Console {msg.type}: {msg.text}") if msg.type in ['error', 'warning'] else None)
        
        # Look for key differences between current and reference
        print(">> Analyzing key differences...")
        
        # Check if current has analytics that reference doesn't
        current_page.set_viewport_size({'width': 1920, 'height': 1080})
        current_page.wait_for_timeout(1000)
        
        current_analytics_attrs = len(current_page.locator('[data-analytics]').all())
        ref_analytics_attrs = len(ref_page.locator('[data-analytics]').all())
        
        if current_analytics_attrs != ref_analytics_attrs:
            results['issues_found'].append(f"Analytics attributes differ: current({current_analytics_attrs}) vs reference({ref_analytics_attrs})")
        
        # Check if CSP and Plausible are additions (these should be preserved)
        has_csp = current_page.locator('meta[http-equiv="Content-Security-Policy"]').count() > 0
        has_plausible = current_page.locator('script[src*="plausible.io"]').count() > 0
        
        if not has_csp:
            results['issues_found'].append("CSP header missing - should be preserved from current implementation")
        
        if not has_plausible:
            results['issues_found'].append("Plausible analytics script missing - should be preserved")

        # Brand compliance checks
        print(">> Checking brand compliance...")
        
        results['brand_compliance'] = {}
        
        # Check brand colors
        current_styles = current_page.evaluate("() => getComputedStyle(document.documentElement).getPropertyValue('--accent').trim()")
        results['brand_compliance']['accent_color'] = {
            'current': current_styles,
            'expected': '#F0B429',
            'match': current_styles.lower() == '#f0b429'
        }
        
        # Check tagline
        hero_text = current_page.locator('.hero-h1').inner_text()
        tagline_match = 'framed' in hero_text.lower() and 'story' in hero_text.lower()
        results['brand_compliance']['tagline'] = {
            'current': hero_text,
            'contains_brand_elements': tagline_match,
            'match': tagline_match
        }
        
        # Check font family
        font_family = current_page.evaluate("() => getComputedStyle(document.body).fontFamily")
        inter_used = 'inter' in font_family.lower()
        results['brand_compliance']['typography'] = {
            'current': font_family,
            'inter_used': inter_used,
            'match': inter_used
        }
        
        # Check logo format
        logo_text = current_page.locator('.nav-logo').inner_html()
        correct_logo = 'FRAME' in logo_text and '<span' in logo_text and 'D</span>' in logo_text
        results['brand_compliance']['logo'] = {
            'current': logo_text,
            'correct_format': correct_logo,
            'match': correct_logo
        }
        
        browser.close()
        
        return results

def generate_report(results):
    """Generate a comprehensive QA report"""
    
    print("\n" + "="*80)
    print(">> FRAMED LANDING PAGE QA REPORT")
    print(">> Verifying current index.html against reference design and brand guidelines")
    print("="*80)
    
    # Visual Comparison Results
    print("\n>> VISUAL COMPARISON")
    print("-" * 40)
    
    for test_name, test_data in results['visual_comparison'].items():
        status = "[PASS]" if test_data.get('match', False) else "[FAIL]"
        print(f"{status} {test_name.replace('_', ' ').title()}")
        
        if not test_data.get('match', False):
            print(f"   Current: {test_data.get('current', 'N/A')}")
            print(f"   Reference: {test_data.get('reference', 'N/A')}")
    
    # Telegram Links
    print(f"\n>> TELEGRAM LINKS ({len(results['telegram_links'])} found)")
    print("-" * 40)
    
    for link in results['telegram_links']:
        status = "[OK]" if link['visible'] and link['href'] == '#telegram' else "[FAIL]"
        print(f"{status} Link {link['index']}: '{link['text']}' -> {link['href']}")
    
    # Checkout Flow
    print("\n>> CHECKOUT FLOW")
    print("-" * 40)
    
    if 'error' in results['checkout_flow']:
        print(f"[ERROR] Error: {results['checkout_flow']['error']}")
    else:
        modal_status = "[OK]" if results['checkout_flow'].get('modal_opens', False) else "[FAIL]"
        print(f"{modal_status} Modal opens: {results['checkout_flow'].get('modal_opens', False)}")
        
        if 'modal_elements' in results['checkout_flow']:
            for element, visible in results['checkout_flow']['modal_elements'].items():
                status = "[OK]" if visible else "[FAIL]"
                print(f"   {status} {element.replace('_', ' ').title()}: {visible}")
    
    # Analytics Check
    print("\n>> ANALYTICS & SECURITY")
    print("-" * 40)
    
    for check, result in results['analytics_check'].items():
        status = "[OK]" if result else "[FAIL]"
        print(f"{status} {check.replace('_', ' ').title()}: {result}")
    
    # Responsive Test
    print("\n>> RESPONSIVE DESIGN")
    print("-" * 40)
    
    for viewport, data in results['responsive_test'].items():
        print(f">> {viewport.title()} ({data['viewport']})")
        for element, visible in data.items():
            if element != 'viewport':
                status = "[OK]" if visible else "[FAIL]"
                print(f"   {status} {element.replace('_', ' ').title()}: {visible}")
    
    # Issues Found
    print("\n>> ISSUES FOUND")
    print("-" * 40)
    
    if results['issues_found']:
        for i, issue in enumerate(results['issues_found'], 1):
            print(f"{i}. {issue}")
    else:
        print("[OK] No issues found!")
    
    # Brand Compliance
    print("\n>> BRAND COMPLIANCE")
    print("-" * 40)
    
    if 'brand_compliance' in results:
        for check, data in results['brand_compliance'].items():
            status = "[OK]" if data.get('match', False) else "[FAIL]"
            print(f"{status} {check.replace('_', ' ').title()}: {data.get('match', False)}")
            
            if not data.get('match', False):
                print(f"   Current: {data.get('current', 'N/A')}")
                if 'expected' in data:
                    print(f"   Expected: {data.get('expected', 'N/A')}")
    
    # Summary
    print("\n>> SUMMARY")
    print("-" * 40)
    
    total_tests = 0
    passed_tests = 0
    
    # Count visual comparison tests
    for test_data in results['visual_comparison'].values():
        total_tests += 1
        if test_data.get('match', False):
            passed_tests += 1
    
    # Count other tests
    if results['checkout_flow'].get('modal_opens', False):
        passed_tests += 1
    total_tests += 1
    
    for result in results['analytics_check'].values():
        total_tests += 1
        if result:
            passed_tests += 1
    
    # Telegram links test
    working_links = sum(1 for link in results['telegram_links'] if link['visible'] and link['href'] == '#telegram')
    total_tests += len(results['telegram_links'])
    passed_tests += working_links
    
    pass_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"Tests Passed: {passed_tests}/{total_tests}")
    print(f"Pass Rate: {pass_rate:.1f}%")
    print(f"Critical Issues: {len(results['issues_found'])}")
    
    # Overall status
    if pass_rate >= 90 and len(results['issues_found']) == 0:
        print("\n🎉 STATUS: READY FOR PRODUCTION")
    elif pass_rate >= 80:
        print("\n⚠️  STATUS: MINOR ISSUES - REVIEW REQUIRED")
    else:
        print("\n🚫 STATUS: MAJOR ISSUES - FIXES REQUIRED")
    
    print("\n📸 Screenshots generated:")
    print("  - qa_current_full.png (Current full page)")
    print("  - qa_reference_full.png (Reference full page)")
    print("  - qa_current_mobile.png (Current mobile view)")
    print("  - qa_current_tablet.png (Current tablet view)")
    
    return results

if __name__ == "__main__":
    print(">> Starting Framed Landing Page QA Validation...")
    
    try:
        results = test_landing_page_comparison()
        final_results = generate_report(results)
        
        # Save detailed results to JSON
        with open('E:/paperclip/_HEYFRAMED/qa_results.json', 'w', encoding='utf-8') as f:
            json.dump(final_results, f, indent=2, ensure_ascii=False)
        
        print(f"\n>> Detailed results saved to: qa_results.json")
        
    except Exception as e:
        print(f"\n>> QA validation failed: {e}")
        raise