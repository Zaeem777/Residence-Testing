import re
from playwright.sync_api import Page, expect


def test_incorrect_credentials(page: Page) -> None:
    page.goto("https://residencedevadmin.smartcitypk.com/login")
    page.get_by_role("textbox", name="Email Address").click()
    page.get_by_role("textbox", name="Email Address").fill("rizmalik979@gmail.com")
    page.get_by_role("textbox", name="Email Address").press("Tab")
    page.get_by_role("textbox", name="Password").fill("zaeem123")
    page.get_by_role("button", name="Login").click()
    # You could assert an error message here if app shows one


def test_empty_password(page: Page) -> None:
    page.goto("https://residencedevadmin.smartcitypk.com/login")
    page.get_by_role("textbox", name="Email Address").click()
    page.get_by_role("textbox", name="Email Address").fill("mam@smartcitypk.com")
    page.get_by_role("button", name="Login").click()

    password_input = page.get_by_role("textbox", name="Password")
    is_valid = password_input.evaluate("el => el.checkValidity()")
    assert not is_valid

    message = password_input.evaluate("el => el.validationMessage")
    print("Validation message:", message)
    assert "fill" in message.lower()
    expect(page).to_have_url("https://residencedevadmin.smartcitypk.com/login")


def test_empty_email(page: Page) -> None:
    page.goto("https://residencedevadmin.smartcitypk.com/login")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("zaeem133")
    page.get_by_role("button", name="Login").click()

    email_input = page.get_by_role("textbox", name="Email Address")
    is_valid = email_input.evaluate("el => el.checkValidity()")
    assert not is_valid

    message = email_input.evaluate("el => el.validationMessage")
    print("Validation message:", message)
    assert "fill" in message.lower()
    expect(page).to_have_url("https://residencedevadmin.smartcitypk.com/login")


def test_correct_credentials(page: Page) -> None:
    page.goto("https://residencedevadmin.smartcitypk.com/login")
    page.get_by_role("textbox", name="Email Address").click()
    page.get_by_role("textbox", name="Email Address").fill("mam@smartcitypk.com")
    page.get_by_role("textbox", name="Email Address").press("Tab")
    page.get_by_role("textbox", name="Password").fill("malik1122")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://residencedevadmin.smartcitypk.com/")
