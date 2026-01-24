from pages.buttons_page import ButtonsPage  # Adjust path as needed

BASE_URL = "https://demoqa.com"

@given('I am on the buttons page')
def step(context):
    context.driver.get(f"{BASE_URL}/buttons")
    context.buttons_page = ButtonsPage(context.driver)  # Initialize page object
    print("✅ Buttons page loaded")

@when('I click the double click button')
def step(context):
    context.buttons_page.double_click_button()

@when('I right click the right click button')
def step(context):
    context.buttons_page.right_click_button()

@when('I click the dynamic click button')
def step(context):
    context.buttons_page.dynamic_click_button()

@then('I see all button messages')
def step(context):
    context.buttons_page.verify_all_messages()
