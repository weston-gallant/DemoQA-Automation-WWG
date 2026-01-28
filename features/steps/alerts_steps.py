from behave import given, when, then
from selenium.common.exceptions import NoAlertPresentException
from pages.alerts_page import AlertsPage
from data.alerts_data import CONFIRM_RESULT_OK, CONFIRM_RESULT_CANCEL


BASE_URL = "https://demoqa.com"


@given('I am on the alerts page')
def step_impl(context):
    context.alerts_page = AlertsPage(context.driver)
    context.alerts_page.go_to_alerts_page(BASE_URL)


@when('I trigger the simple alert')
def step_impl(context):
    context.alerts_page.click_simple_alert()


@then('I can accept the simple alert')
def step_impl(context):
    context.alerts_page.wait_for_alert_and_accept()


@when('I trigger the delayed alert')
def step_impl(context):
    context.alerts_page.click_timer_alert()


@then('I can accept the delayed alert when it appears')
def step_impl(context):
    context.alerts_page.wait_for_delayed_alert_and_accept()


@when('I trigger the confirm alert')
def step_impl(context):
    context.alerts_page.click_confirm_alert()


@when('I accept the confirm alert')
def step_impl(context):
    # Try to accept immediately; fallback to explicit wait if needed
    try:
        alert = context.driver.switch_to.alert
        print(f"ℹ️ Alert text: {alert.text}")
        alert.accept()
        print("✅ Confirm alert accepted (direct)")
    except NoAlertPresentException:
        context.alerts_page.wait_for_alert_and_accept()


@when('I dismiss the confirm alert')
def step_impl(context):
    context.alerts_page.wait_for_alert_and_dismiss()


@then('I see the confirm result text "{expected_text}"')
def step_impl(context, expected_text):
    # Feature text drives expectation; constants keep it DRY in code
    if expected_text == CONFIRM_RESULT_OK:
        context.alerts_page.assert_confirm_result_equals(CONFIRM_RESULT_OK)
    elif expected_text == CONFIRM_RESULT_CANCEL:
        context.alerts_page.assert_confirm_result_equals(CONFIRM_RESULT_CANCEL)
    else:
        context.alerts_page.assert_confirm_result_equals(expected_text)


@when('I trigger the prompt alert')
def step_impl(context):
    context.alerts_page.click_prompt_alert()


@when('I enter "{name}" into the prompt alert')
def step_impl(context, name):
    context.prompt_name = name
    context.alerts_page.wait_for_alert_and_send_keys(name, accept=True)


@then('I see the prompt result text "You entered {name}"')
def step_impl(context, name):
    context.alerts_page.assert_prompt_result_contains(name)


@when('I enter "{name}" into the prompt alert but dismiss it')
def step_impl(context, name):
    context.prompt_name = name
    context.alerts_page.wait_for_alert_and_send_keys(name, accept=False)


@then('I do not see any prompt result text')
def step_impl(context):
    context.alerts_page.assert_no_prompt_result()
