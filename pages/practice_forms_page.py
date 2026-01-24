from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    
    def fill_required_fields(self, user_data=PRACTICE_FORM_DEFAULT_USER):
        """Fill DemoQA Practice Form required fields with provided data"""
        self.driver.find_element(*self.first_name).send_keys(user_data["first_name"])
        self.driver.find_element(*self.last_name).send_keys(user_data["last_name"])
        self.driver.find_element(*self.user_email).send_keys(user_data["email"])
        self.driver.find_element(*self.gender_male).click()
        self.driver.find_element(*self.user_number).send_keys(user_data["phone"])
        print("✅ Practice form required fields filled")
    
    def submit_form(self):
        submit_btn = self.driver.find_element(*self.submit_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        self.driver.execute_script("arguments[0].click();", submit_btn)
        print("✅ Form submitted")
    
    def verify_success_message(self):
        self.wait.until(lambda driver: "Thanks for submitting" in driver.page_source)
        print("✅ SUCCESS verified!")
    
    def close_modal(self):
        self.driver.find_element(*self.close_modal_btn).click()
        self.wait.until_not(EC.visibility_of_element_located(self.modal_header))
        print("✅ Modal closed and verified gone")
