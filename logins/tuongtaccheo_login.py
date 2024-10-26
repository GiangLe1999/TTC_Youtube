# logins/tuongtaccheo_login.py

from seleniumbase import SB
from config.constants import TUONGTACCHEO_USERNAME

def login_tuongtaccheo(sb: SB, username, password):
    sb.open("https://tuongtaccheo.com/")
    sb.sleep(20)
    sb.wait_for_element('input#name', timeout=10)
    sb.type('input#name', username)
    sb.type('input[type="password"]', password)
    sb.click('input[type="submit"]')
    sb.sleep(3)  # Wait for login to complete
