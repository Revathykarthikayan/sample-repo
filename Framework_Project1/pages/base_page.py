from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # constructor method
    def __init__(self, driver):
        self.driver = driver

    # method to find element
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # method to click element
    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    # method to enter text
    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    # method to get current url
    def get_current_url(self):
        return self.driver.current_url
