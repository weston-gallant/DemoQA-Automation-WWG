from behave import given, when, then
from pages.checkboxes_page import CheckboxesPage
from data.checkboxes_data import CHECKBOX_LABEL_TO_RESULT_KEY


BASE_URL = "https://demoqa.com"


@given('I am on the check box page')
def step_go_to_checkbox_page(context):
    context.driver.get(f"{BASE_URL}/checkbox")
    context.checkboxes_page = CheckboxesPage(context.driver)
    print("✅ Check Box page loaded")


@when('I expand all check boxes')
def step_expand_all_checkboxes(context):
    context.checkboxes_page.expand_all()


@when('I select the "{label}" checkbox')
def step_select_single_checkbox(context, label):
    context.checkboxes_page.select_checkbox_by_label(label)
    context.last_selected_labels = [label]


@when('I select the following check boxes')
def step_select_multiple_checkboxes(context):
    labels = [row["label"] for row in context.table]
    for label in labels:
        context.checkboxes_page.select_checkbox_by_label(label)
    context.last_selected_labels = labels


@when('I select the "{label}" checkbox from check box data')
def step_select_checkbox_from_data(context, label):
    context.checkboxes_page.select_checkbox_by_label(label)
    context.last_selected_labels = [label]


@then('I see "{result_key}" in the selected results')
def step_see_single_result_key(context, result_key):
    context.checkboxes_page.assert_result_contains_key(result_key)


@then('I see all of these in the selected results')
def step_see_all_result_keys(context):
    keys = [row["result_key"] for row in context.table]
    context.checkboxes_page.assert_results_contain_all_keys(keys)
