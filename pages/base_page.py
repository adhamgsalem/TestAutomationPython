
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator):
        element = self.driver.find_element(by, locator)
        element.click()

    def send_keys(self, by, locator, text):
        element = self.driver.find_element(by, locator)
        element.send_keys(text)

    def get_element_text(self, by, locator):
        element = self.driver.find_element(by, locator)
        return element.text

    def wait_for_element(self, by, locator, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))
