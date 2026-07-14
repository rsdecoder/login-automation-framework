# Login Automation Framework

Automated UI tests for the login functionality of a web application, built with
**Python, Playwright, and pytest** using the **Page Object Model**.

The tests run against [SauceDemo](https://www.saucedemo.com), a public demo site
made for automation practice. They cover both positive (successful login) and
negative (locked-out user, wrong credentials, empty fields) scenarios.

## Tech stack

- **Python 3** – programming language
- **Playwright** – browser automation (drives a real Chromium browser)
- **pytest** – test runner
- **pytest-playwright** – connects Playwright to pytest
- **pytest-html** – generates an HTML test report

## Project structure

```
login-automation-framework/
├── pages/
│   └── login_page.py      # Page Object: locators and actions for the login page
├── tests/
│   └── test_login.py      # The login tests (positive + negative)
├── test_data/
│   └── users.py           # Credentials and test data, kept separate from the tests
├── conftest.py            # Shared pytest fixtures (browser settings, logging)
├── pytest.ini             # Configuration (base URL, reporting, logging)
├── requirements.txt       # Python dependencies
└── README.md
```

## Setup

You need **Python 3.9 or newer** installed (developed on Python 3.13).

1. Clone the repository and move into it:
   ```bash
   git clone <repository-url>
   cd login-automation-framework
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the browser Playwright needs:
   ```bash
   playwright install chromium
   ```

## Running the tests

Run all tests:
```bash
pytest
```

Some useful options:

| Command | What it does |
|---|---|
| `pytest -v` | Verbose – shows each test name and result |
| `pytest --headed` | Shows the browser while the tests run |
| `pytest -k login` | Runs only tests whose name contains "login" |

After a run, two outputs are produced:

- **HTML report:** `reports/report.html` – open it in a browser to see the results.
- **Log file:** `reports/test_run.log` – a timestamped record of the run.

## Test scenarios

| Test | Type | Expected result |
|---|---|---|
| Valid credentials | Positive | Redirected to the inventory page |
| Locked-out user | Negative | Error: "this user has been locked out" |
| Wrong credentials | Negative | Error: username/password do not match |
| Empty username | Negative | Error: "Username is required" |
| Empty password | Negative | Error: "Password is required" |

## Design choices

- **Page Object Model** – each page is a class that holds its locators and actions.
  Tests call methods like `login()` instead of using selectors directly, so if the
  page changes I only update one file (`pages/login_page.py`).

- **Test data kept separate** – credentials live in `test_data/users.py`, not inside
  the tests, so the data is easy to find and change.

- **Parametrization for the negative cases** – the four invalid-login scenarios share
  the same steps, so they are written as one parametrized test rather than four
  copies. pytest still reports each case separately.

- **Auto-waiting assertions** – I use Playwright's `expect()` assertions, which retry
  until the condition is met or they time out. This avoids fragile `sleep()` calls.

- **Logging** – the page actions and a start/end marker per test are logged to the
  console and a file, using Python's `logging` module. Passwords are never logged.

- **Screenshots, video, and traces on failure** – configured in `pytest.ini` so that
  when a test fails there is enough information to debug it.

## Improvements with more time

- Run the tests across more browsers (Firefox and WebKit, which Playwright supports
  out of the box).
- Add a CI pipeline (e.g. GitHub Actions) to run the tests automatically on every push.
- Add more scenarios, such as logging out and session handling.
- Add Allure reporting for a richer, historical view of test runs.
