import os
import requests
from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@fixture
def browser_fixture(context):
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

    # Cache driver for a few days to reduce CI network flakiness
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)

    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.maximize_window()
    context.driver.set_page_load_timeout(20)

    print("✅ Browser ready - ONE browser for entire suite")
    yield context.driver

    # Teardown
    if hasattr(context, "driver"):
        context.driver.quit()
        print("✅ Browser closed - suite complete")


def before_all(context):
    use_fixture(browser_fixture, context)

def before_scenario(context, scenario):
    """
    Lightweight health check: if DemoQA is unreachable from CI/local,
    skip the scenario instead of hard-failing with long timeouts.
    """
    try:
        resp = requests.get("https://demoqa.com", timeout=5)
        if resp.status_code >= 500:
            scenario.skip("DemoQA is unavailable (5xx from demoqa.com)")
    except requests.RequestException:
        scenario.skip("DemoQA is unreachable from current environment")
