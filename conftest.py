import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        browser.close()


@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    page.set_default_timeout(60000)  # 60s for all actions
    page.set_default_navigation_timeout(60000)  # 60s for navigation
    yield page
    page.close()


@pytest.fixture
def logged_in_page(browser_context):
    """Page that logs in before yielding."""
    page = browser_context.new_page()
    page.set_default_timeout(1200000)  # 60s for all actions
    page.set_default_navigation_timeout(1200000)  # 60s for navigation
    page.goto(f"{BASE_URL}/login")
    page.get_by_role("textbox", name="Email Address").click()
    page.fill("input[name='email']", ADMIN_EMAIL)
    page.get_by_role("textbox", name="Email Address").press("Tab")
    page.fill("input[name='password']", ADMIN_PASSWORD)
    page.get_by_role("button", name="Login").click()

    page.wait_for_url(f"{BASE_URL}/")
    yield page
    page.close()
