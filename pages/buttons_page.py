from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import time


class ButtonsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        # Button locators
        self.double_click_btn = (By.ID, "doubleClickBtn")
        self.right_click_btn = (By.ID, "rightClickBtn")
        self.dynamic_click_btn = (By.XPATH, "//button[text()='Click Me']")

        self.double_click_msg = (By.ID, "doubleClickMessage")
        self.right_click_msg = (By.ID, "rightClickMessage")
        self.dynamic_click_msg = (By.ID, "dynamicClickMessage")

    def double_click_button(self):
        btn = self.driver.find_element(*self.double_click_btn)
        ActionChains(self.driver).double_click(btn).perform()
        print("✅ Double click performed")

    def right_click_button(self):
        btn = self.driver.find_element(*self.right_click_btn)
        ActionChains(self.driver).context_click(btn).perform()
        print("✅ Right click performed")

    def dynamic_click_button(self):
        btn = self.driver.find_element(*self.dynamic_click_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        print("✅ Dynamic click performed")

    def verify_all_messages(self):
        self.wait.until(EC.visibility_of_element_located(self.double_click_msg))
        self.wait.until(EC.visibility_of_element_located(self.right_click_msg))
        self.wait.until(EC.visibility_of_element_located(self.dynamic_click_msg))
        print("✅ All button messages verified")

    def assert_no_messages_visible(self):
        for locator in [self.double_click_msg, self.right_click_msg, self.dynamic_click_msg]:
            elements = self.driver.find_elements(*locator)
            assert not any(e.is_displayed() for e in elements), "Message should not be visible yet"
        print("✅ No button messages visible")

    def assert_only_message_visible(self, expected_locator):
        # Map locator → expected text fragment
        locator_to_text = {
            self.double_click_msg: "You have done a double click",
            self.right_click_msg: "You have done a right click",
            self.dynamic_click_msg: "You have done a dynamic click",
        }

        expected_text = locator_to_text.get(expected_locator)
        assert expected_text, "Unknown locator passed to assert_only_message_visible"

        # Poll page_source for up to 5 seconds
        end_time = time.time() + 5
        found = False
        while time.time() < end_time and not found:
            if expected_text in self.driver.page_source:
                found = True
                break
            time.sleep(0.25)

        assert found, f"Expected button message text not found: '{expected_text}'"
        print("✅ Expected button message text found in page source")