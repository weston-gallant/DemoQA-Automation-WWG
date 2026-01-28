from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data.practice_form_data import PRACTICE_FORM_DEFAULT_USER


class PracticeFormsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        # Form locators
        self.first_name = (By.ID, "firstName")
        self.last_name = (By.ID, "lastName")
        self.user_email = (By.ID, "userEmail")
        self.gender_male = (By.XPATH, "//label[@for='gender-radio-1']")
        self.user_number = (By.ID, "userNumber")
        self.submit_btn = (By.ID, "submit")
        self.close_modal_btn = (By.ID, "closeLargeModal")
        self.modal_header = (By.CLASS_NAME, "modal-header")

        # Optional
        self.required_error_fields = (By.CSS_SELECTOR, ".was-validated .is-invalid")

    def fill_required_fields(self, user_data=PRACTICE_FORM_DEFAULT_USER):
        """Fill DemoQA Practice Form required fields with provided data"""
        self.driver.find_element(*self.first_name).send_keys(user_data["first_name"])
        self.driver.find_element(*self.last_name).send_keys(user_data["last_name"])
        self.driver.find_element(*self.user_email).send_keys(user_data["email"])

        gender_el = self.driver.find_element(*self.gender_male)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", gender_el)
        self.driver.execute_script("arguments[0].click();", gender_el)

        self.driver.find_element(*self.user_number).send_keys(user_data["phone"])
        print("✅ Practice form required fields filled")

    def fill_with_custom_data(self, user_data):
        self.driver.find_element(*self.first_name).clear()
        self.driver.find_element(*self.last_name).clear()
        self.driver.find_element(*self.user_email).clear()
        self.driver.find_element(*self.user_number).clear()

        self.driver.find_element(*self.first_name).send_keys(user_data["first_name"])
        self.driver.find_element(*self.last_name).send_keys(user_data["last_name"])
        self.driver.find_element(*self.user_email).send_keys(user_data["email"])
        self.driver.find_element(*self.user_number).send_keys(user_data["phone"])

        gender_el = self.driver.find_element(*self.gender_male)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", gender_el)
        self.driver.execute_script("arguments[0].click();", gender_el)

        print("✅ Practice form filled with custom data")

    def submit_form(self):
        submit_btn = self.driver.find_element(*self.submit_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        self.driver.execute_script("arguments[0].click();", submit_btn)
        print("✅ Form submitted")

    def verify_success_message(self):
        self.wait.until(lambda d: "Thanks for submitting" in d.page_source)
        print("✅ SUCCESS verified!")

    def close_modal(self):
        close_btn = self.driver.find_element(*self.close_modal_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", close_btn)
        self.driver.execute_script("arguments[0].click();", close_btn)
        self.wait.until_not(EC.visibility_of_element_located(self.modal_header))
        print("✅ Modal closed and verified gone")

    def verify_required_field_errors(self):
        """Verify that the form was NOT submitted when required fields are empty."""
        try:
            self.wait.until(lambda d: "Thanks for submitting" in d.page_source)
            raise AssertionError(
                "Form submitted successfully, but should have failed due to empty required fields"
            )
        except TimeoutException:
            pass

        assert "automation-practice-form" in self.driver.current_url, \
            "Expected to remain on the practice form page after invalid submit"
        print("✅ Required-field submission prevented (no success modal)")
