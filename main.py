from seleniumbase import SB
from config.constants import (
    GOOGLE_EMAIL,
    GOOGLE_PASSWORD,
    TUONGTACCHEO_USERNAME,
    TUONGTACCHEO_URL,
    MAX_ITERATIONS,
)
from logins.google_login import login_google
from logins.tuongtaccheo_login import login_tuongtaccheo
from actions.comment_actions import post_comments
from actions.nhan_tien_actions import click_nhan_tien_buttons


import time

from selenium.webdriver.common.by import By

def main(count):
    with SB(uc=True, headless=True) as sb:
        login_google(sb, GOOGLE_EMAIL[count], GOOGLE_PASSWORD[count])

        sb.sleep(25)

        print(f"Login Gmail {GOOGLE_EMAIL[count]} thành công")
            
        login_tuongtaccheo(sb, TUONGTACCHEO_USERNAME[count], "Giang19111999@")

        print(f"Login TK TTC {TUONGTACCHEO_USERNAME[count]} thành công")

        money = sb.get_text("#soduchinh")
        print(f"Số dư trước khi chạy: {money}")
        
        for iteration in post_comments(sb, TUONGTACCHEO_URL, MAX_ITERATIONS):
            click_nhan_tien_buttons(sb)
            sb.sleep(4)
        
        money = sb.get_text("#soduchinh")
        print(f"Số dư sau khi chạy xong: {money}")

        sb.sleep(5)
            

if __name__ == "__main__":
    repeat_times = 100  # Số lần lặp lại toàn bộ đoạn code

    for i in range(repeat_times):
        print(f"=== Lần lặp thứ {i + 1} ===")

        count = 0
        for tuongtaccheo_step in GOOGLE_EMAIL:
            print(f"Bắt đầu chạy TK TTC {TUONGTACCHEO_USERNAME[count]}")
            main(count)
            print(f"Kết thúc chạy TK TTC {TUONGTACCHEO_USERNAME[count]} sau {MAX_ITERATIONS} vòng")
            count += 1
            time.sleep(5)

        print("=== Completed ===")

