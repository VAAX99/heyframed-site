from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Enable console logging
    page.on('console', lambda msg: print(f'Console: {msg.type}: {msg.text}'))
    
    page.goto('file:///E:/paperclip/_HEYFRAMED/index.html')
    page.wait_for_load_state('networkidle')
    
    print('Page loaded successfully')
    
    # Check if checkout buttons exist
    checkout_buttons = page.locator('button[onclick*="openCheckout"]').count()
    print(f'Checkout buttons found: {checkout_buttons}')
    
    if checkout_buttons > 0:
        # Try to click the first one
        try:
            page.locator('button[onclick*="openCheckout"]').first.click()
            time.sleep(2)
            
            # Check modal state
            modal_exists = page.locator('#checkoutModal').count()
            modal_visible = page.locator('#checkoutModal.open').count()
            
            print(f'Modal exists: {modal_exists}')
            print(f'Modal with open class: {modal_visible}')
            
            # Check modal style
            if modal_exists > 0:
                modal_style = page.locator('#checkoutModal').get_attribute('style')
                print(f'Modal style: {modal_style}')
                
                modal_class = page.locator('#checkoutModal').get_attribute('class')
                print(f'Modal classes: {modal_class}')
            
        except Exception as e:
            print(f'Error clicking checkout: {e}')
    
    browser.close()