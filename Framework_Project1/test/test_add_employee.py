import pytest
from pages.login_page import LoginPage
from pages.add_employee import AddEmployee
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# setting up the test environment
@pytest.mark.usefixtures("setup")
class TestAddEmpPage:

    def test_add_emp(self):
        # creating instance and passing the WebDriver to login, add_employee page
        login_page = LoginPage(self.driver)
        add_employee = AddEmployee(self.driver)

        # passing arguments to the methods in login page
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        # calling every method of add_employee page
        add_employee.go_to_add_employee()
        add_employee.add_first_name("Aswin")
        add_employee.add_middle_name("Rachel")
        add_employee.add_last_name("Marks")
        add_employee.add_id("100009")
        add_employee.click_save()

        # Wait until the URL contains 'view personal details' or timeout after 30 seconds
        WebDriverWait(self.driver, 30).until(EC.url_contains("viewPersonalDetails"))

        assert "viewPersonalDetails" in self.driver.current_url

        # calling methods to update personal details of employee
        add_employee.licence_number("AK89084")
        add_employee.nationality("Indian")
        add_employee.status("Married")
        add_employee.dob("1995-01-09")
        add_employee.blood_group("O+")
        add_employee.click_save_2()
