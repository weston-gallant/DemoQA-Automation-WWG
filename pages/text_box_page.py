from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.text_box_data import TEXT_BOX_DEFAULT_USER


class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        self.full_name = (By.ID, "userName")
        self.email = (By.ID, "userEmail")
        self.current_address = (By.ID, "currentAddress")
        self.permanent_address = (By.ID, "permanentAddress")
        self.submit_btn = (By.ID, "submit")

        # Output locators
        self.output_name = (By.ID, "name")
        self.output_email = (By.ID, "email")
        self.output_current_address = (By.XPATH, "//p[@id='currentAddress']")
        self.output_permanent_address = (By.XPATH, "//p[@id='permanentAddress']")

    def fill_with_default_user(self, user_data=TEXT_BOX_DEFAULT_USER):
        self.fill_form(user_data)
        print("✅ Text Box filled with default user")

    def fill_form(self, user_data):
        self.driver.find_element(*self.full_name).clear()
        self.driver.find_element(*self.email).clear()
        self.driver.find_element(*self.current_address).clear()
        self.driver.find_element(*self.permanent_address).clear()

        self.driver.find_element(*self.full_name).send_keys(user_data["full_name"])
        self.driver.find_element(*self.email).send_keys(user_data["email"])
        self.driver.find_element(*self.current_address).send_keys(user_data["current_address"])
        self.driver.find_element(*self.permanent_address).send_keys(user_data["permanent_address"])

    def submit_form(self):
        submit = self.driver.find_element(*self.submit_btn)
        # Scroll into view to avoid being hidden/covered
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit)
        # Click via JS to bypass ad overlays intercepting the click
        self.driver.execute_script("arguments[0].click();", submit)
        print("✅ Text Box form submitted")

    def verify_output_matches(self, user_data):
        self.wait.until(EC.visibility_of_element_located(self.output_name))

        name_text = self.driver.find_element(*self.output_name).text
        email_text = self.driver.find_element(*self.output_email).text
        current_text = self.driver.find_element(*self.output_current_address).text
        permanent_text = self.driver.find_element(*self.output_permanent_address).text

        assert user_data["full_name"] in name_text
        assert user_data["email"] in email_text
        assert user_data["current_address"] in current_text
        assert user_data["permanent_address"] in permanent_text

        print("✅ Text Box output matches input")
