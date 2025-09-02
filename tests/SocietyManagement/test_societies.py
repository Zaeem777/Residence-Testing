import uuid
from playwright.sync_api import Page, expect


def test_societies(logged_in_page: Page) -> None:
    logged_in_page.goto("https://residencedevadmin.smartcitypk.com/")
    logged_in_page.get_by_role("link", name=" Society Management ").click()
    logged_in_page.get_by_role("link", name="Societies").click()

    unique_name = f"ZA-{uuid.uuid4().hex[:6]}"

    logged_in_page.get_by_role("button", name=" Add").first.click()
    logged_in_page.get_by_role("textbox", name="Add Sector Name").fill(unique_name)
    logged_in_page.get_by_role("button", name="Submit").click()

    logged_in_page.get_by_role("button", name=" View").first.click()
    expect(logged_in_page.get_by_text(unique_name).first).to_be_visible()
    logged_in_page.locator("#kt_modal_loadData").get_by_text("Close").click()
