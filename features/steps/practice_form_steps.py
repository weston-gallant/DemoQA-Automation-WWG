from behave import given, when, then
from pages.practice_forms_page import PracticeFormsPage
from data.practice_form_data import PRACTICE_FORM_USERS_BY_KEY


BASE_URL = "https://demoqa.com"

@given('I am on the practice forms page')
def step_impl(context):
    context.driver.get(f"{BASE_URL}/automation-practice-form")
    context.forms_page = PracticeFormsPage(context.driver)
    print("✅ DemoQA loaded")


@when('I fill in the required fields')
def step_impl(context):
    context.forms_page.fill_required_fields()


@then('I see a success message')
def step_impl(context):
    context.forms_page.submit_form()
    context.forms_page.verify_success_message()


@then('I close the modal')
def step_impl(context):
    context.forms_page.close_modal()


@when('I submit the form without filling required fields')
def step_impl(context):
    # Just submit the blank form
    context.forms_page.submit_form()


@then('I see validation errors for required fields')
def step_impl(context):
    context.forms_page.verify_required_field_errors()


@when('I fill the practice form for "{user_key}" from practice form data')
def step_impl(context, user_key):
    user = PRACTICE_FORM_USERS_BY_KEY[user_key]
    context.forms_page.fill_with_custom_data(user)
