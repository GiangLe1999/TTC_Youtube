# actions/nhan_tien_actions.py

from seleniumbase import SB

def click_nhan_tien_buttons(sb: SB):
    try:
        while True:
            # Find all 'Nhận tiền' buttons currently present
            nhan_tien_buttons = sb.find_elements('button:contains("Nhận tiền")')
            if not nhan_tien_buttons:
                break  # Exit the loop if no buttons are left
            
            for idx, button in enumerate(nhan_tien_buttons, start=1):
                try:
                    button.click()
                    sb.sleep(3)  # Wait for 3 seconds before the next click
                except Exception as e:
                    x = 1
                    continue  # Continue with the next button if there's an error
            
            # Optional: Refresh the list in case new buttons have loaded after clicking
            sb.sleep(2)
    
    except Exception as e:
        x = 1
