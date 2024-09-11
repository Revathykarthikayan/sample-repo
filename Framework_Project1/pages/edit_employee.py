from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class EditEmployee(BasePage):
    # locators are given for elements used in EditEmployee class
    PIM = (By.XPATH, '//span[text()="PIM"]')
    INFO_BUTTON = (By.XPATH, '//i[@class="oxd-icon bi-caret-down-fill"]')
    HINTS = (By.XPATH, '(//div[@class="oxd-autocomplete-wrapper"])[1]')
    ID = (By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')
    SEARCH_BUTTON = (By.XPATH, '//button[text()=" Search "]')
    EDIT = (By.XPATH, '(//i[@class="oxd-icon bi-pencil-fill"])[1]')
    MIDDLE_NAME = (By.XPATH, '//input[@placeholder="Middle Name"]')
    SAVE_BUTTON = (By.XPATH, '(//button[text()=" Save "])[1]')
    success_toast_message = (By.XPATH, "//div[@id='oxd-toaster_1']")

    try:
        # Navigating to edit employee page from dashboard page
        def go_to_edit_employee(self):
            self.click_element(self.PIM)

            # Wait until the URL contains 'dashboard' or timeout after 30 seconds
            WebDriverWait(self.driver, 10).until(EC.url_contains("viewEmployeeList"))

            assert "viewEmployeeList" in self.driver.current_url

            # Wait until the element is clickable and  then click it

            WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.
                                           INFO_BUTTON)).click()

            # Giving input for ID of the employee to be searched
        def enter_id(self, emp):

            # Wait for the element to be visible then send keys

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.
                                               ID)).send_keys(emp)

            # Clicking search button
        def search(self):

            self.click_element(self.SEARCH_BUTTON)

            # Clicking edit icon of employee searched
        def edit(self):

            # Wait until the element is clickable and  then click it

            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(self.
                                               EDIT))
            self.click_element(self.EDIT)

            # Editing the middle name of the employee
        def change_middle_name(self, middle_name):

            # Wait for the element to be visible,clear it then send keys

            new_text = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.MIDDLE_NAME))
            new_text.send_keys(Keys.BACKSPACE * len(new_text.get_attribute("value")))
            new_text.send_keys(middle_name)

            # clicking save button to save change
        def save_changes(self):

            # Wait for the element to be visible,clear it then send keys

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.
                                               SAVE_BUTTON))

        # Printing success message
            print("Middle name of employee is edited successfully")

        # Printing exception message if occurred
    except Exception as e:
        print(f"exception occurred in edit employee  : {e}")
