import re
from playwright.sync_api import Page, expect
import time


def test_dashboard(page: Page) -> None:
    page.goto("https://residencedevadmin.smartcitypk.com/")
    # page.get_by_role("textbox", name="Email Address").fill("mam@smartcitypk.com")
    # page.get_by_role("textbox", name="Email Address").press("Tab")
    # page.get_by_role("textbox", name="Password").fill("malik1122")
    # page.get_by_role("button", name="Login").click()
    time.sleep(6)
    page.get_by_text("Welcome, Tech Admin T").click()
    page.get_by_role("link", name=" My Profile Account settings").click()
    page.get_by_role("link", name="Change Password").click()
    page.locator("#password").click()
    page.get_by_role("link", name="Cancel").click()
    page.get_by_role("link", name="Dashboard").click()
