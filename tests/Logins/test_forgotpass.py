import re
from playwright.sync_api import Page, expect


def test_invalid_email_shows_error(page: Page) -> None:
    page.goto("https://residencedevadmin.smartcitypk.com/forgot-password")
    page.get_by_role("textbox", name="Email Address").click()
    page.get_by_role("textbox", name="Email Address").fill("dummy@invalid.com")
    page.get_by_role("button", name="Send Password Reset Link").click()
    expect(page.get_by_text("We can't find a user with")).to_be_visible()


def test_sql_injection(page: Page) -> None:
    page.goto("https://residencedevadmin.smartcitypk.com/forgot-password")
    page.get_by_role("textbox", name="Email Address").click()
    page.get_by_role("textbox", name="Email Address").fill("' OR '1'='1")
    page.get_by_role("button", name="Send Password Reset Link").click()
    expect(page.get_by_text("The email must be a valid email address")).to_be_visible()


def test_valid_email_shows_success(page: Page) -> None:
    page.goto("https://residencedevadmin.smartcitypk.com/forgot-password")
    page.get_by_role("textbox", name="Email Address").click()
    page.get_by_role("textbox", name="Email Address").fill("rizmalik979@gmail.com")
    page.get_by_role("button", name="Send Password Reset Link").click()
    expect(page.get_by_text("We have emailed your password")).to_be_visible()
