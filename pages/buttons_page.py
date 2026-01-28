from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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
        btn.click()
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
        locators = {
            "double": self.double_click_msg,
            "right": self.right_click_msg,
            "dynamic": self.dynamic_click_msg,
        }
        for key, locator in locators.items():
            elements = self.driver.find_elements(*locator)
            visible = any(e.is_displayed() for e in elements)
            if locator == expected_locator:
                assert visible, f"{key} message should be visible"
            else:
                assert not visible, f"{key} message should NOT be visible"
        print("✅ Only expected message visible")
