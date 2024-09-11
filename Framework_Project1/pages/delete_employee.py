from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage



class DeleteEmployee(BasePage):
    # locators are given for elements used in AddEmployee class
    PIM = (By.XPATH, '//span[text()="PIM"]')
    LIST_BUTTON = (By.XPATH, '//a[text() = "Employee List"]')
    INFO_BUTTON = (By.XPATH, '//i[@class="oxd-icon bi-caret-down-fill"]')
    HINTS = (By.XPATH, '(//div[@class="oxd-autocomplete-wrapper"])[1]')
    ID = (By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')
    SEARCH_BUTTON = (By.XPATH, '//button[text()=" Search "]')
    TRASH = (By.XPATH, '//i[@class="oxd-icon bi-trash"][1]')
    DELETE = (
        By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]')

    try:
        # Navigating to edit employee page from dashboard page
        def go_to_delete_employee(self):
            self.click_element(self.PIM)

            # Wait until the URL contains 'dashboard' or timeout after 30 seconds
            WebDriverWait(self.driver, 10).until(EC.url_contains("viewEmployeeList"))

            assert "viewEmployeeList" in self.driver.current_url

            WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.
                                           INFO_BUTTON)).click()

            # Giving input for ID of the employee to be searched
        def enter_id(self, emp):

            # Wait for the element to be visible then send keys

            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(self.
                                               ID)).send_keys(emp)

            # Clicking search button
        def search(self):
            self.click_element(self.SEARCH_BUTTON)

            # Clicking trash icon to delete employee
        def delete(self):

            # Wait for the element to be visible then send keys

            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(self.TRASH
                                               ))
            self.click_element(self.TRASH)

            # Clicking popup to delete employee
        def popup(self):

            # Wait for the element to be visible then click it

            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(self.DELETE
                                               ))
            self.click_element(self.DELETE)

            # Printing success message
            print("Employee details deleted successfully")

    except Exception as e:
        print(f"exception occurred in delete employee page  : {e}")
