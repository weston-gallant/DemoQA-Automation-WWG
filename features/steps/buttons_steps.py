from behave import given, when, then
from pages.buttons_page import ButtonsPage

BASE_URL = "https://demoqa.com"
# Triggering run

@given('I am on the buttons page')
def step_go_to_buttons_page(context):
    context.driver.get(f"{BASE_URL}/buttons")
    context.buttons_page = ButtonsPage(context.driver)
    print("✅ Buttons page loaded")


@then('I do not see any button messages')
def step_no_button_messages(context):
    context.buttons_page.assert_no_messages_visible()


@when('I click the double click button')
def step_click_double(context):
    context.buttons_page.double_click_button()


@then('I see the double click message only')
def step_double_message_only(context):
    context.buttons_page.assert_only_message_visible(
        context.buttons_page.double_click_msg
    )


@when('I right click the right click button')
def step_right_click(context):
    context.buttons_page.right_click_button()


@then('I see the right click message only')
def step_right_click_message_only(context):
    context.buttons_page.assert_only_message_visible(
        context.buttons_page.right_click_msg
    )


@when('I click the dynamic click button')
def step_dynamic_click(context):
    context.buttons_page.dynamic_click_button()


@then('I see the dynamic click message only')
def step_dynamic_message_only(context):
    context.buttons_page.assert_only_message_visible(
        context.buttons_page.dynamic_click_msg
    )