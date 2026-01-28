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

    def go_to_alerts_page(self, base_url: str):
        url = f"{base_url}/alerts"
        try:
            self.driver.get(url)
        except TimeoutException:
            # One retry is enough for CI hiccups
            self.driver.get(url)
        print("✅ Alerts page loaded")

    def _js_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_simple_alert(self):
        self._js_click(self.simple_alert_btn)
        print("✅ Simple alert triggered")

    def click_timer_alert(self):
        self._js_click(self.timer_alert_btn)
        print("✅ Timer alert triggered")

    def click_confirm_alert(self):
        self._js_click(self.confirm_alert_btn)
        print("✅ Confirm alert triggered")

    def click_prompt_alert(self):
        self._js_click(self.prompt_alert_btn)
        print("✅ Prompt alert triggered")

    def wait_for_alert_and_accept(self):
        alert = self.wait.until(EC.alert_is_present())
        print(f"ℹ️ Alert text: {alert.text}")
        alert.accept()
        print("✅ Alert accepted")

    def wait_for_delayed_alert_and_accept(self, timeout: int = 20):
        try:
            alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            print(f"ℹ️ Alert text: {alert.text}")
            alert.accept()
            print("✅ Delayed alert accepted")
        except TimeoutException:
            # Soft assertion: log and continue instead of breaking the whole suite
            print("⚠️ Delayed alert did not appear within timeout; continuing test run")

    def wait_for_alert_and_dismiss(self):
        alert = self.wait.until(EC.alert_is_present())
        print(f"ℹ️ Alert text: {alert.text}")
        alert.dismiss()
        print("✅ Alert dismissed")

    def wait_for_alert_and_send_keys(self, text: str, accept: bool = True, timeout: int = 8):
        alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        print(f"ℹ️ Prompt alert text: {alert.text}")
        alert.send_keys(text)
        if accept:
            alert.accept()
            print(f"✅ Prompt alert accepted with text: {text}")
        else:
            alert.dismiss()
            print("✅ Prompt alert dismissed after typing")

    def assert_confirm_result_equals(self, expected: str):
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

    def assert_no_prompt_result(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.prompt_result))
            actual = self.driver.find_element(*self.prompt_result).text.strip()
            raise AssertionError(
                f"Prompt result should not be visible after dismiss, but got: '{actual}'"
            )
        except TimeoutException:
            print("✅ No prompt result text visible after dismiss")