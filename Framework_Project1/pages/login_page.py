from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # initializing webdriver for login page
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, '//button[@type="submit"]')
        self.error_message = (By.CSS_SELECTOR, '.error-message')

    try:
        # compatibility of the browser is checked
        def compatibility(self):
            try:
                warning_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'unsupported browser')]")
                assert not warning_message.is_displayed(), "Unsupported browser warning detected."

            except NoSuchElementException:
                # If no warning is found, assume compatibility is okay
                pass

        # method to enter username
        def enter_username(self, username):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field)).send_keys(
                username)

        # method to enter password
        def enter_password(self, password):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_field)).send_keys(
                password)

        # method to click login button
        def click_login(self):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

        #   calling the above methods to perform login
        def login(self, username, password):
            self.enter_username(username)
            self.enter_password(password)
            self.click_login()

        # printing exception message if occurred
    except Exception as e:
        print(f"exception occurred in employee addition : {e}")
