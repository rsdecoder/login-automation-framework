import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Default settings for every browser context the tests run in.

    pytest-playwright creates a fresh, isolated browser context per test
    (its own cookies/storage), which gives us clean setup/teardown for free.
    Here we just standardise the window size so screenshots are consistent.
    """
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }
