"""Test data for the login tests, kept separate from the test logic.

These are the public demo credentials documented on https://www.saucedemo.com.
"""

VALID_USER = {
    "username": "standard_user",
    "password": "secret_sauce",
}

LOCKED_OUT_USER = {
    "username": "locked_out_user",
    "password": "secret_sauce",
}

INVALID_USER = {
    "username": "wrong_user",
    "password": "wrong_password",
}
