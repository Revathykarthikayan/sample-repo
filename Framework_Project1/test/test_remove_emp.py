import pytest
from pages.login_page import LoginPage
from pages.delete_employee import DeleteEmployee


# setting up the test environment
@pytest.mark.usefixtures("setup")
class TestAddEmpPage:
    def test_remove_emp(self):
        # creating instance and passing the WebDriver to login, add_employee page
        login_page = LoginPage(self.driver)
        delete_employee = DeleteEmployee(self.driver)

        # passing arguments to the methods in login page
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        # calling every method of delete_employee page
        delete_employee.go_to_delete_employee()
        delete_employee.enter_id("100009")
        delete_employee.search()
        delete_employee.delete()
        delete_employee.popup()
