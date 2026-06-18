from playwright.sync_api import expect

from pages.login_page import LoginPage
from test_data.users import VALID_USER


def test_valid_login_redirects_to_inventory(page):
    """A user with valid credentials is taken to the inventory page."""
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    # Playwright's expect() waits/retries until the URL matches (or times out),
    # so we don't need a manual sleep after clicking "Login".
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
