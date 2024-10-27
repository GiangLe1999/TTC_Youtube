# actions/comment_actions.py

from selenium.webdriver.common.by import By
from seleniumbase import SB
import time

def sub_cheo(sb: SB, tuongtaccheo_url: str, max_iterations: int = 100):
    iteration = 0  # Initialize iteration counter
    
    while iteration < max_iterations:
        iteration += 1
        
        # === Navigate to YouTube Comment Page ===
        try:
            sb.open(tuongtaccheo_url)
            sb.wait_for_element("div.col-md-2.col-xs-6", timeout=15)
            # print("debug 1")
            
            # === Find All Target Divs ===
            target_divs = sb.find_elements("div.col-md-2.col-xs-6")

            # print("debug 2")
            
            # === Iterate Through Each Div and Comment ===
            for idx, div in enumerate(target_divs, start=1):
                try:
                    # === Find and Retrieve Text from Textarea ===
                    
                    # print("debug 3")
                    # === Click 'BÌNH LUẬN' Button ===
                    binhluan_button = div.find_element(By.XPATH, './/b[contains(text(), " ĐĂNG KÝ")]')
                    # print("debug 4")
                    binhluan_button.click()
                    # print("debug 5")
                    sb.sleep(5)  # Brief pause to allow UI to update
                    sb.switch_to_window(1)
                    sb.sleep(5)
                    # === Scroll if Necessary ===
                    
                    # === Check for 'yt-formatted-string#simplebox-placeholder' ===
                    try:
                        # print("debug 6")
                        sb.wait_for_element('button.ytp-play-button.ytp-button', timeout=5)
                        sb.click('button.ytp-play-button.ytp-button')
                    except Exception:
                        # print("debug 6.1")
                        sb.click('button.ytp-skip-ad-button')
                        sb.wait_for_element('button.ytp-play-button.ytp-button', timeout=5)
                        sb.click('button.ytp-play-button.ytp-button')
                    

                    sb.sleep(15)

                    sb.click('yt-button-shape#subscribe-button-shape')

                    # dangky_button = div.find_element("yt-button-shape#subscribe-button-shape")
                    # dangky_button.click()

                    sb.sleep(5)  # Wait for the comment to be posted
                    
                    sb.driver.close()
                    sb.switch_to_window(0) 
                
                except Exception as e:
                    x = 1
                    print('sub_cheo_youtube.py')
                    print(e)
                    # Attempt to ensure we're back to the main window
                    try:
                        sb.driver.close()
                        sb.switch_to_window(0)
                    except:
                        pass
                    continue  # Continue with the next div if there's an error
        except:
            print('skip')
        
        # === Final Actions After Commenting ===
        sb.sleep(10)
        
        yield iteration  # Yield control back to main for further actions