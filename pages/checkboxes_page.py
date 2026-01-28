from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckboxesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        self.expand_all_btn = (By.CSS_SELECTOR, "button[title='Expand all']")
        self.checkbox_tree = (By.CLASS_NAME, "check-box-tree")  # container
        self.result_panel = (By.ID, "result")

    def open(self):
        # For symmetry with other pages if you want, but not strictly needed
        pass

    def expand_all(self):
        self.wait.until(EC.element_to_be_clickable(self.expand_all_btn)).click()
        print("✅ Expanded all check boxes")

    def select_checkbox_by_label(self, label_text: str):
        xpath = f"//span[@class='rct-title' and text()='{label_text}']"
        locator = (By.XPATH, xpath)
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        print(f"✅ Selected checkbox: {label_text}")

    def get_selected_result_text(self) -> str:
        self.wait.until(EC.visibility_of_element_located(self.result_panel))
        return self.driver.find_element(*self.result_panel).text.lower()

    def assert_result_contains_key(self, key: str):
        text = self.get_selected_result_text()
        assert key in text, f"Expected result to contain '{key}', but got: {text}"
        print(f"✅ Result contains key: {key}")

    def assert_results_contain_all_keys(self, keys):
        text = self.get_selected_result_text()
        for key in keys:
            assert key in text, f"Expected result to contain '{key}', but got: {text}"
        print(f"✅ Result contains all keys: {keys}")
