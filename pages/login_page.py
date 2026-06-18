class LoginPage:
    """Page Object for the SauceDemo login page.

    Tests interact with the page through this class instead of using raw
    selectors, so if the markup changes we only update it in one place.
    """

    # Path relative to the base_url configured in pytest.ini.
    PATH = "/"

    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

    def navigate(self):
        """Open the login page."""
        self.page.goto(self.PATH)

    def login(self, username, password):
        """Fill in the credentials and submit the form."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        """Return the text of the error banner shown on a failed login."""
        return self.error_message.text_content()
