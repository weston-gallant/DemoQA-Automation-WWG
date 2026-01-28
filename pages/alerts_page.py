from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data.alerts_data import CONFIRM_RESULT_OK, CONFIRM_RESULT_CANCEL, PROMPT_RESULT_PREFIX


class AlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Buttons
        self.simple_alert_btn = (By.ID, "alertButton")
        self.timer_alert_btn = (By.ID, "timerAlertButton")
        self.confirm_alert_btn = (By.ID, "confirmButton")
        self.prompt_alert_btn = (By.ID, "promtButton")

        # Result texts
        self.confirm_result = (By.ID, "confirmResult")
        self.prompt_result = (By.ID, "promptResult")

    def click_simple_alert(self):
        self.driver.find_element(*self.simple_alert_btn).click()
        print("✅ Simple alert triggered")

    def click_timer_alert(self):
        self.driver.find_element(*self.timer_alert_btn).click()
        print("✅ Timer alert triggered")

    def click_confirm_alert(self):
        self.driver.find_element(*self.confirm_alert_btn).click()
        print("✅ Confirm alert triggered")

    def click_prompt_alert(self):
        self.driver.find_element(*self.prompt_alert_btn).click()
        print("✅ Prompt alert triggered")

    def wait_for_alert_and_accept(self):
        alert = self.wait.until(EC.alert_is_present())
        print(f"ℹ️ Alert text: {alert.text}")
        alert.accept()
        print("✅ Alert accepted")

    def wait_for_alert_and_dismiss(self):
        alert = self.wait.until(EC.alert_is_present())
        print(f"ℹ️ Alert text: {alert.text}")
        alert.dismiss()
        print("✅ Alert dismissed")

    def wait_for_alert_and_send_keys(self, text: str, accept: bool = True):
        alert = self.wait.until(EC.alert_is_present())
        print(f"ℹ️ Prompt alert text: {alert.text}")
        alert.send_keys(text)
        if accept:
            alert.accept()
            print(f"✅ Prompt alert accepted with text: {text}")
        else:
            alert.dismiss()
            print("✅ Prompt alert dismissed after typing")

    def assert_confirm_result_equals(self, expected: str):
        # Wait for confirm result to appear
        element = self.wait.until(EC.visibility_of_element_located(self.confirm_result))
        actual = element.text.strip()
        assert actual == expected, f"Expected confirm result '{expected}', got '{actual}'"
        print(f"✅ Confirm result text matches: {actual}")

    def assert_prompt_result_contains(self, name: str):
        element = self.wait.until(EC.visibility_of_element_located(self.prompt_result))
        actual = element.text.strip()
        expected = f"{PROMPT_RESULT_PREFIX}{name}"
        assert actual == expected, f"Expected prompt result '{expected}', got '{actual}'"
        print(f"✅ Prompt result text matches: {actual}")

    def wait_for_alert_and_send_keys(self, text: str, accept: bool = True):
        alert = self.wait.until(EC.alert_is_present())
        print(f"ℹ️ Prompt alert text: {alert.text}")
        alert.send_keys(text)
        if accept:
            alert.accept()
            print(f"✅ Prompt alert accepted with text: {text}")
        else:
            alert.dismiss()
            print("✅ Prompt alert dismissed after typing")

    def assert_no_prompt_result(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.prompt_result))
            # If we get here, text appeared (failure for this scenario)
            actual = self.driver.find_element(*self.prompt_result).text.strip()
            raise AssertionError(
                f"Prompt result should not be visible after dismiss, but got: '{actual}'"
            )
        except TimeoutException:
            # Expected: no prompt result
            print("✅ No prompt result text visible after dismiss")

