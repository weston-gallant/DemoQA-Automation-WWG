from behave import given, when, then
from pages.buttons_page import ButtonsPage

BASE_URL = "https://demoqa.com"


@given('I am on the buttons page')
def step_impl(context):
    context.driver.get(f"{BASE_URL}/buttons")
    context.buttons_page = ButtonsPage(context.driver)
    print("✅ Buttons page loaded")


@when('I click the double click button')
def step_impl(context):
    context.buttons_page.double_click_button()


@when('I right click the right click button')
def step_impl(context):
    context.buttons_page.right_click_button()


@when('I click the dynamic click button')
def step_impl(context):
    context.buttons_page.dynamic_click_button()


@then('I see all button messages')
def step_impl(context):
    context.buttons_page.verify_all_messages()


@then('I do not see any button messages')
def step_impl(context):
    context.buttons_page.assert_no_messages_visible()


@then('I see the double click message only')
def step_impl(context):
    context.buttons_page.assert_only_message_visible(context.buttons_page.double_click_msg)


@then('I see the right click message only')
def step_impl(context):
    context.buttons_page.assert_only_message_visible(context.buttons_page.right_click_msg)


@then('I see the dynamic click message only')
def step_impl(context):
    context.buttons_page.assert_only_message_visible(context.buttons_page.dynamic_click_msg)
