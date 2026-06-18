"""Test data for the login tests, kept separate from the test logic.

These are the public demo credentials documented on https://www.saucedemo.com.
"""

# The happy-path user used by the positive test.
VALID_USER = {
    "username": "standard_user",
    "password": "secret_sauce",
}

# Negative scenarios for the parametrized test.
# Each row is: (username, password, expected_error_message)
INVALID_LOGIN_CASES = [
    (
        "locked_out_user",
        "secret_sauce",
        "Epic sadface: Sorry, this user has been locked out.",
    ),
    (
        "wrong_user",
        "wrong_password",
        "Epic sadface: Username and password do not match any user in this service",
    ),
    (
        "",
        "secret_sauce",
        "Epic sadface: Username is required",
    ),
    (
        "standard_user",
        "",
        "Epic sadface: Password is required",
    ),
]
