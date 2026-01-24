from pages.practice_forms_page import PracticeFormsPage  # Adjust path as needed

BASE_URL = "https://demoqa.com"

@given('I am on the practice forms page')
def step(context):
    context.driver.get(f"{BASE_URL}/automation-practice-form")
    context.forms_page = PracticeFormsPage(context.driver)
    print("✅ DemoQA loaded")

@when('I fill in the required fields')
def step(context):
    context.forms_page.fill_required_fields()

@then('I see a success message')
def step(context):
    context.forms_page.submit_form()
    context.forms_page.verify_success_message()

@then('I close the modal')
def step(context):
    context.forms_page.close_modal()
