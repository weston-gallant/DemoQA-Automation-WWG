from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# We start our test and open the browser
@given('I am on the practice forms page')
def step(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.get("https://demoqa.com/automation-practice-form")
    print("✅ DemoQA loaded")

@when('I fill in the required fields')
def step(context):
    # We fill out required fields in the form
    context.driver.find_element(By.ID, "firstName").send_keys("Weston")
    context.driver.find_element(By.ID, "lastName").send_keys("Gallant")
    context.driver.find_element(By.ID, "userEmail").send_keys("DJWestyOwn@test.com")
    # We select gender
    context.driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()
    # We input phone number
    context.driver.find_element(By.ID, "userNumber").send_keys("1234567890")
    # We scroll down and click "submit"
    submit_btn = context.driver.find_element(By.ID, "submit")
    context.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    time.sleep(1)  # Brief pause for stability (Will remove in the future for reactivity)
    context.driver.execute_script("arguments[0].click();", submit_btn)
    print("✅ Form submitted")

@then('I see a success message')
def step(context):
    time.sleep(3)  # Wait for modal to appear
    page_source = context.driver.page_source
    assert "Thanks for submitting" in page_source
    print("✅ SUCCESS verified!")

@then('I close the modal')
def step(context):    
    # We want to close the pop-up modal after
    context.driver.find_element(By.ID, "closeLargeModal").click()
    # Using the below wait, I can replace other waits to make them more dynamic
    WebDriverWait(context.driver, 5).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "modal-header")))
    print("✅ Modal closed and verified gone")
    context.driver.quit()
