from behave import given, when, then
from pages.text_box_page import TextBoxPage
from data.text_box_data import TEXT_BOX_DEFAULT_USER, TEXT_BOX_USERS_BY_KEY

BASE_URL = "https://demoqa.com"


@given('I am on the text box page')
def step_impl(context):
    context.driver.get(f"{BASE_URL}/text-box")
    context.text_box_page = TextBoxPage(context.driver)
    print("✅ Text Box page loaded")


@when('I fill in the text box with default user data')
def step_impl(context):
    context.text_box_page.fill_with_default_user()


@when('I fill the text box form for "{user_key}" from text box data')
def step_impl(context, user_key):
    user = TEXT_BOX_USERS_BY_KEY[user_key]
    context.text_box_page.fill_form(user)
    context.text_box_user = user  # stash for later verification


@when('I submit the text box form')
def step_impl(context):
    context.text_box_page.submit_form()


@then('I see the text box output matching the input')
def step_impl(context):
    user = getattr(context, "text_box_user", TEXT_BOX_DEFAULT_USER)
    context.text_box_page.verify_output_matches(user)
