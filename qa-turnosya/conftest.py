import os
import base64
import urllib.request
from pathlib import Path
from urllib.parse import urlparse
from uuid import uuid4

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


REPORTS_DIR = Path(__file__).parent / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default=os.getenv("TURNOSYA_BASE_URL", "http://127.0.0.1:5000"),
        help="URL base de una instancia local desechable de TurnosYa.",
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url").rstrip("/")


@pytest.fixture
def driver(request):
    options = Options()
    if os.getenv("QA_HEADLESS", "1") != "0":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)
    metadata = getattr(request.config, "_metadata", None)
    if metadata is not None:
        metadata["Navegador"] = f"{browser.name} {browser.capabilities.get('browserVersion', 'desconocida')}"
    browser.implicitly_wait(0)
    yield browser
    browser.quit()


def _reset_local_test_instance(base_url):
    parsed = urlparse(base_url)
    if parsed.hostname not in {"localhost", "127.0.0.1", "::1"}:
        pytest.fail("Por seguridad, el fixture de limpieza solo admite localhost.")
    with urllib.request.urlopen(f"{base_url}/test/reset", timeout=5) as response:
        if response.status != 200:
            pytest.fail(f"La limpieza de datos respondió HTTP {response.status}.")


@pytest.fixture(autouse=True)
def clean_test_data(base_url):
    REPORTS_DIR.mkdir(exist_ok=True)
    SCREENSHOTS_DIR.mkdir(exist_ok=True)
    _reset_local_test_instance(base_url)
    yield
    _reset_local_test_instance(base_url)


@pytest.fixture
def user_factory(driver, base_url):
    from pages.auth_page import AuthPage

    def create_user():
        user = {
            "name": "QA TurnosYa",
            "email": f"qa-{uuid4().hex}@example.test",
            "password": "Temporal-QA-123!",
        }
        auth = AuthPage(driver, base_url)
        auth.register(user["name"], user["email"], user["password"])
        auth.login(user["email"], user["password"])
        return user

    return create_user


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    browser = item.funcargs.get("driver")
    if browser is None:
        return

    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    screenshot = SCREENSHOTS_DIR / f"{item.name}.png"
    if browser.save_screenshot(str(screenshot)):
        report.sections.append(("Captura de pantalla", str(screenshot)))
        extras = getattr(report, "extras", [])
        image_data = base64.b64encode(screenshot.read_bytes()).decode("ascii")
        extras.append(
            pytest_html.extras.image(image_data, name="Captura del fallo", mime_type="image/png")
        )
        report.extras = extras