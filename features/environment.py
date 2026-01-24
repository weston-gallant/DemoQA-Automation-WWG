from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    """Runs ONCE before ALL scenarios in the suite"""
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    print("✅ Browser ready - ONE browser for entire suite")

def after_all(context):
    """Runs ONCE after ALL scenarios complete"""
    if hasattr(context, 'driver'):
        context.driver.quit()
        print("✅ Browser closed - suite complete")
