import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.login_page import LoginPage


# opening the csv file to read and execute test data
def get_login_data():
    login_data = []
    with open('data/login_data.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row['username']
            password = row['password']
            login_data.append((username, password))
        return login_data


# setting up the test environment
@pytest.mark.usefixtures("setup")
class TestLogin:
    # using parametrize marker to pass data into test_login
    @pytest.mark.parametrize("username, password", get_login_data())
    def test_login(self, username, password):
        # creating instance and passing the WebDriver to login
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        # Wait until the URL contains 'dashboard' or timeout after 30 seconds
        WebDriverWait(self.driver, 5).until(EC.url_contains("dashboard"))

        assert "dashboard" in self.driver.current_url
