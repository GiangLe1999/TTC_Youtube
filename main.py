# main.py

from seleniumbase import SB
from config.constants import (
    GOOGLE_EMAIL,
    GOOGLE_PASSWORD,
    TUONGTACCHEO_USERNAME,
    TUONGTACCHEO_URL,
    # MAX_ITERATIONS,
    # SUBCHEOYOUTUBE_URL,
    # MAX__SUB_YOUTUBE_ITERATIONS
)
from logins.google_login import login_google
from logins.tuongtaccheo_login import login_tuongtaccheo
from actions.comment_actions import post_comments
from actions.nhan_tien_actions import click_nhan_tien_buttons
# from actions.nhan_tien_sub_cheo import click_nhan_tien_sub_cheo_buttons
# from actions.sub_cheo_youtube import sub_cheo

import time

from selenium.webdriver.common.by import By

def main(count):
    with SB(uc=True) as sb:
        login_google(sb, GOOGLE_EMAIL[count], GOOGLE_PASSWORD[count])

        sb.sleep(20)
            
        # === TuongTacCheo Login ===
        login_tuongtaccheo(sb, TUONGTACCHEO_USERNAME[count], "Giang19111999@")

        money = sb.get_text("#soduchinh")
        print(f"= Số dư đầu: {money} =")
        
        for iteration in post_comments(sb, TUONGTACCHEO_URL, 2):
            
            # === Click All 'Nhận tiền' Buttons with 3-Second Interval ===
            click_nhan_tien_buttons(sb)
            
            # === Check if 'Nhận tiền' Buttons Were Found and Clicked ===
            # (Đã được xử lý trong hàm click_nhan_tien_buttons)
            
            # === Optional: Wait Before Starting the Next Iteration ===
            sb.sleep(4)
        
        # === Final Actions After All Iterations ===
        money = sb.get_text("#soduchinh")
        print(f"= Số dư cuối: {money} =")

        sb.sleep(5)
        # === Keep the Browser Open for Observation if Needed ===
        # sb.sleep(60)
            

if __name__ == "__main__":
    count = 0
    for tuongtaccheo_step in GOOGLE_EMAIL:
        print(f"=== Bắt đầu tương tác với account {TUONGTACCHEO_USERNAME[count]} Completed ===")
        main(count)
        count = count + 1
        print(f"=== Kết thúc tương tác với account {TUONGTACCHEO_USERNAME[count]} Completed ===")
        time.sleep(5)

    print("=== Completed ===") 

