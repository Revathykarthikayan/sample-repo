import pytest
from pages.login_page import LoginPage
from pages.edit_employee import EditEmployee


# setting up the test environment
@pytest.mark.usefixtures("setup")
class TestEditPage:
    def test_edit_emp(self):
        login_page = LoginPage(self.driver)
        edit_employee = EditEmployee(self.driver)
        # passing arguments to the methods in login page
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        # calling every method of edit_employee page
        edit_employee.go_to_edit_employee()
        edit_employee.enter_id("100009")
        edit_employee.search()
        edit_employee.edit()
        edit_employee.change_middle_name("Gimme")
        edit_employee.save_changes()
