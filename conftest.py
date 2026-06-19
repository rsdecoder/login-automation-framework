import logging

import pytest

logger = logging.getLogger(__name__)


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


@pytest.fixture(autouse=True)
def log_test_boundaries(request):
    """Log a clear start/end marker around every test.

    autouse=True means this runs for every test automatically, without the
    test having to ask for it. The code before yield is setup, the code after
    is teardown -- so we get a tidy START/END pair in the log per test.
    """
    logger.info("===== START test: %s =====", request.node.name)
    yield
    logger.info("===== END test:   %s =====", request.node.name)
