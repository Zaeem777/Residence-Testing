import re
from playwright.sync_api import Page, expect


def test_logout(logged_in_page: Page) -> None:
    expect(logged_in_page.get_by_text("Welcome, Tech Admin T")).to_be_visible()
    logged_in_page.get_by_text("Welcome, Tech Admin T").click()
    logged_in_page.get_by_role("link", name="Logout").click()
    expect(logged_in_page).to_have_url(
        "https://residencedevadmin.smartcitypk.com/login"
    )
