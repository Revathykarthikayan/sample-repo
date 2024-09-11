from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class AddEmployee(BasePage):

    # locators are given for elements used in AddEmployee class
    PIM = (By.XPATH, '//span[text()="PIM"]')
    ADD_BUTTON = (By.XPATH, '// a[text() = "Add Employee"]')
    FIRST_NAME = (By.XPATH, '//input[@placeholder="First Name"]')
    MIDDLE_NAME = (By.XPATH, '//input[@placeholder="Middle Name"]')
    LAST_NAME = (By.XPATH, '//input[@placeholder="Last Name"]')
    ID = (By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')
    SAVE_BUTTON_1 = (By.XPATH, '// button[text() = " Save "]')
    LICENSE = (By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[4]')
    NATIONALITY = (By.XPATH, '(//div[text()="-- Select --"])[1]')
    M_STATUS = (By.XPATH, '(//div[text()="-- Select --"])[2]')
    DOB = (By.XPATH, '//input[@placeholder="yyyy-dd-mm"]')
    BLOOD_GROUP = (By.XPATH, '(//div[text()="-- Select --"])[1]')
    GENDER = (By.XPATH, '//label[text()="Male"]')
    SAVE_BUTTON_2 = (By.XPATH, '// button[text() = " Save "]')
    success_toast_message = (By.XPATH, "//div[@id='oxd-toaster_1']")

    try:
        # Navigates to add employee page from dashboard page
        def go_to_add_employee(self):
            self.click_element(self.PIM)
            self.click_element(self.ADD_BUTTON)

            #  Giving input for first name

        def add_first_name(self, first_name):

            # Wait for the element to clickable then send keys

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.FIRST_NAME)
            ).send_keys(first_name)

            #  Giving input for middle name

        def add_middle_name(self, middle_name):

            # Wait for the element to be clickable then send keys

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.MIDDLE_NAME)
            ).send_keys(middle_name)

            #  Giving input for last name

        def add_last_name(self, last_name):

            # Wait for the element to be located then send keys
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.LAST_NAME)
            ).send_keys(last_name)

        #  Giving input for employee ID
        def add_id(self, emp_id):

            # Wait for the element to be located, then send keys
            id_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.ID))

            # clearing the ID text field to sendkeys
            id_text.send_keys(Keys.BACKSPACE * len(id_text.get_attribute("value")))
            id_text.send_keys(emp_id)

            #  Clicking save button after entering the basic details of the employee

        def click_save(self):

            # Wait for the element to be clickable then click it
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.SAVE_BUTTON_1)
            ).click()
            print("New employee added successfully")

            #  Giving input for licence number

        def licence_number(self, license_no):

            # Wait for the element to be clickable then send keys
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.LICENSE)
            ).send_keys(license_no)

            #  Giving input for nationality of employee

        def nationality(self, nationality):

            # Wait for the element to be visible then send keys
            WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.NATIONALITY)
            ).send_keys(nationality)

            #  Giving input for marital status

        def status(self, status_m):

            # Wait for the element to be visible then send keys
            WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.M_STATUS)
            ).send_keys(status_m)

            #  Giving input for first name

        def dob(self, dob):

            # Wait for the element to be clickable then send keys

            WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.DOB)
            ).send_keys(dob)

            #  Giving input for blood group

        def blood_group(self, rh):

            # Wait for the element to be visible then send keys

            WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.BLOOD_GROUP)
            ).send_keys(rh)

        #  clicking save button after entering the personal details of the employee
        def click_save_2(self):

            # Wait for the element to be clickable then send keys
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.SAVE_BUTTON_2))

            # Printing success message
            print("New employee details updated successfully")

            # printing exception message if occurred
    except Exception as e:
        print(f"exception occurred in employee addition : {e}")
