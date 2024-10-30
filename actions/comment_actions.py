# actions/comment_actions.py

from selenium.webdriver.common.by import By
from seleniumbase import SB
import time

def post_comments(sb: SB, tuongtaccheo_url: str, max_iterations: int = 100):
    iteration = 0  # Initialize iteration counter
    
    while iteration < max_iterations:
        iteration += 1
        
        # === Navigate to YouTube Comment Page ===
        sb.open(tuongtaccheo_url)
        sb.wait_for_element("div.col-md-3.col-xs-12", timeout=5)
        
        # === Find All Target Divs ===                                    
        target_divs = sb.find_elements("div.col-md-3.col-xs-12")
        
        # === Iterate Through Each Div and Comment ===
        for idx, div in enumerate(target_divs, start=1):
            try:
                # === Find and Retrieve Text from Textarea ===
                textarea = div.find_element(By.TAG_NAME, "textarea")
                comment_text = textarea.get_attribute("value")
                
                # === Click 'BÌNH LUẬN' Button ===
                binhluan_button = div.find_element(By.XPATH, './/button[contains(text(), "BÌNH LUẬN")]')
                binhluan_button.click()
                sb.sleep(5)  # Brief pause to allow UI to update
                sb.switch_to_window(1)
                sb.sleep(5)

                try:
                    sb.wait_for_element('button.ytp-play-button.ytp-button', timeout=5)
                    sb.click('button.ytp-play-button.ytp-button')
                except Exception:
                    print("debug 2")

                sb.sleep(5)

                # === Scroll if Necessary ===
                sb.execute_script("window.scrollBy(0, 300);")

                sb.sleep(5)
                
                # === Check for 'yt-formatted-string#simplebox-placeholder' ===
                try:
                    sb.wait_for_element('yt-formatted-string#simplebox-placeholder', timeout=30)
                except Exception:
                    print("debug 3")
                    sb.driver.close()
                    sb.switch_to_window(0)
                    continue  # Skip to the next div
                
                # === Click the Placeholder to Activate Comment Box ===
                sb.click('yt-formatted-string#simplebox-placeholder')
                
                # === Type the Comment ===
                sb.wait_for_element('div#contenteditable-root', timeout=30)
                sb.type('div#contenteditable-root', comment_text)
                sb.sleep(5)  # Brief pause before submitting
                
                # === Click 'Comment' Button ===
                sb.click('button:contains("Comment")')
                sb.sleep(10)  # Wait for the comment to be posted
                
                sb.driver.close()
                sb.switch_to_window(0) 

                # sb.sleep(45)
                # sb.click('button.btn.btn-success')
                # sb.sleep(2)

            
            except Exception as e:
                x = 1
                # Attempt to ensure we're back to the main window
                try:
                    sb.driver.close()
                    sb.switch_to_window(0)
                except:
                    pass
                continue  # Continue with the next div if there's an error
        
        # === Final Actions After Commenting ===
        sb.sleep(45)
        
        yield iteration  # Yield control back to main for further actions
