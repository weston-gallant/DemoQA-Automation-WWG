from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@given('I open browser')
def step(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.get("https://demoqa.com/automation-practice-form")
    print("✅ Browser opened - DemoQA loaded")

@when('I do nothing')
def step(context):
    print("✅ Ready for next step")

@then('test passes')
def step(context):
    assert "Practice Form" in context.driver.page_source
    print("✅ DemoQA verified")
    context.driver.quit()
