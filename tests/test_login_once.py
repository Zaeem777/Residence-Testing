import re
from playwright.sync_api import sync_playwright


def test_save_login_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://residencedevadmin.smartcitypk.com/login")

        # Perform login once
        page.fill("input[name='email']", "mam@smartcitypk.com")
        page.fill("input[name='password']", "malik1122")
        page.click("button[type='submit']")

        # Wait until dashboard loads
        page.wait_for_url("https://residencedevadmin.smartcitypk.com/")

        # Save session to file
        page.context.storage_state(path="storage.json")
        browser.close()


# if __name__ == "__main__":
#     save_login_state()
