import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.maximize_window()


def after_all(context):
    """Runs ONCE after ALL scenarios complete"""
    if hasattr(context, 'driver'):
        context.driver.quit()
        print("✅ Browser closed - suite complete")
