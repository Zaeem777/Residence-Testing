# tests/Departments/test_departments.py
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def logged_in_page(browser_context):
    """Override conftest fixture: create one logged-in page for the entire session (this file)."""
    page = browser_context.new_page()
    page.set_default_timeout(120000)  # 120s
    page.set_default_navigation_timeout(120000)

    page.goto("https://residencedevadmin.smartcitypk.com/login")
    page.get_by_role("textbox", name="Email Address").fill("mam@smartcitypk.com")
    page.get_by_role("textbox", name="Email Address").press("Tab")
    page.fill("input[name='password']", "malik1122")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("https://residencedevadmin.smartcitypk.com/")

    yield page
    # Don’t close here → keep alive for the whole file
    # If you want to close at the end of the session, add page.close() after yield


@pytest.fixture(scope="session")
def unique_name():
    """Generate a unique department name for this session."""
    import uuid

    return f"Testing-{uuid.uuid4().hex[:6]}"


@pytest.mark.order(1)
def test_create_department(logged_in_page: Page, unique_name: str):
    logged_in_page.get_by_role("link", name=" Department ").click()
    logged_in_page.get_by_role("link", name="Departments", exact=True).click()
    logged_in_page.get_by_role("link", name=" Create").click()
    logged_in_page.get_by_role("combobox", name="Select Society").click()
    logged_in_page.locator("#bs-select-1-1").click()
    logged_in_page.locator("label").filter(has_text="Complaint").locator("span").click()
    logged_in_page.locator("label").filter(has_text="Service").locator("span").click()
    logged_in_page.get_by_role("textbox", name="Enter Department Name").fill(
        unique_name
    )
    logged_in_page.get_by_role("button", name="Submit").click()
    expect(logged_in_page.get_by_role("cell", name=unique_name)).to_be_visible()
    print("Department created:", unique_name)


@pytest.mark.order(2)
def test_edit_department(logged_in_page: Page, unique_name: str):
    new_name = f"{unique_name}-Updated"
    logged_in_page.goto(
        "https://residencedevadmin.smartcitypk.com/department/departments"
    )
    #   logged_in_page.get_by_role("link", name=" Department ").click()
    #    logged_in_page.get_by_role("link", name="Departments", exact=True).click()
    logged_in_page.get_by_role("row", name=unique_name).get_by_role(
        "link"
    ).first.click()

    # Update
    logged_in_page.get_by_role("textbox", name="Enter Department Name").fill(new_name)
    logged_in_page.get_by_role("button", name="Submit").click()
    expect(logged_in_page.get_by_role("cell", name=new_name)).to_be_visible()
    print("Department updated to:", new_name)

    # Revert
    logged_in_page.get_by_role("row", name=new_name).get_by_role("link").first.click()
    logged_in_page.get_by_role("textbox", name="Enter Department Name").fill(
        unique_name
    )
    logged_in_page.get_by_role("button", name="Submit").click()
    expect(logged_in_page.get_by_role("cell", name=unique_name)).to_be_visible()
    print("Department name reverted to:", unique_name)


@pytest.mark.order(3)
def test_delete_department(logged_in_page: Page, unique_name: str):
    logged_in_page.goto(
        "https://residencedevadmin.smartcitypk.com/department/departments"
    )
    logged_in_page.get_by_role("row", name=unique_name).get_by_role(
        "link"
        # "button", name="Delete"
    ).nth(1).click()
    logged_in_page.get_by_role("button", name="Delete").click()
    expect(logged_in_page.get_by_text("Data Deleted successfully")).to_be_visible(
        timeout=10000
    )  # 10s

    print("Department deleted:", unique_name)
