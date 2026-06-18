import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from test_data.users import VALID_USER, INVALID_LOGIN_CASES


def test_valid_login_redirects_to_inventory(page):
    """A user with valid credentials is taken to the inventory page."""
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    # Playwright's expect() waits/retries until the URL matches (or times out),
    # so we don't need a manual sleep after clicking "Login".
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.parametrize(
    "username, password, expected_error",
    INVALID_LOGIN_CASES,
    ids=["locked_out_user", "wrong_credentials", "empty_username", "empty_password"],
)
def test_invalid_login_shows_error(page, username, password, expected_error):
    """Invalid logins stay on the login page and show the expected error."""
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(username, password)

    # The error banner should appear with the exact message...
    expect(login_page.error_message).to_have_text(expected_error)
    # ...and we should NOT have been let through to the inventory page.
    expect(page).to_have_url("https://www.saucedemo.com/")
