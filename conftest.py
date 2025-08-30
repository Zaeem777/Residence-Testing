import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="storage.json")
        yield context
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.set_default_timeout(60000)  # 60s for all actions
    page.set_default_navigation_timeout(60000)  # 60s for navigation
    yield page
    page.close()
