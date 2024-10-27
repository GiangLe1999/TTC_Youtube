# logins/google_login.py

from seleniumbase import SB
from config.constants import GOOGLE_EMAIL, GOOGLE_PASSWORD

def login_google(sb: SB, google_email, google_password):
    sb.open("https://accounts.google.com/signin")
    sb.sleep(5)
    sb.type('input[type="email"]', google_email)
    sb.click('button:contains("Next")')
    sb.wait_for_element('input[type="password"]', timeout=1000)
    sb.type('input[type="password"]', google_password)
    sb.click('button:contains("Next")')
    sb.sleep(5)  # Wait for login to complete
