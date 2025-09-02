import re
from playwright.sync_api import Page, expect


def test_dashboard(logged_in_page: Page) -> None:
    logged_in_page.goto("https://residencedevadmin.smartcitypk.com/")
    logged_in_page.get_by_text("Welcome, Tech Admin T").click()
    logged_in_page.get_by_role("link", name=" My Profile Account settings").click()
    logged_in_page.get_by_role("link", name="Change Password").click()
    logged_in_page.locator("#password").click()
    logged_in_page.get_by_role("link", name="Cancel").click()
    logged_in_page.get_by_role("link", name="Dashboard").click()
