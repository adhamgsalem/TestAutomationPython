
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def click(self, by, locator):
        self.logger.info("Clicking on element with locator {locator} using {by}")
        element = self.driver.find_element(by, locator)
        element.click()

    def js_click(self, by, locator):
        self.logger.info("JS Clicking on element with locator {locator} using {by}")
        element = self.driver.find_element(by, locator)
        element.execute_script("arguments[0].click();", element)

    def clear_text_field(self, by, locator):
        self.logger.info("Clearing text of text field with locator {locator} using {by}")
        element = self.driver.find_element(by, locator)
        element.clear()

    def send_keys(self, by, locator, text):
        self.logger.info("Sending text to element with locator {locator} using {by}")
        element = self.driver.find_element(by, locator)
        element.send_keys(text)

    def get_element_text(self, by, locator):
        self.logger.info("Getting text of element with locator {locator} using {by}")
        element = self.driver.find_element(by, locator)
        return element.text

    def wait_for_element_presence(self, by, locator, timeout=10):
        self.logger.info("Waiting for element to be displayed with locator {locator} using {by}")
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))

    def select_from_dropdown(self, by, locator, value):
        self.logger.info("Selecting option {value} from dropdown with locator {locator} using {by}")
        element = self.driver.find_element(by, locator)
        select = Select(element)
        select.select_by_visible_text(value)

    def drag_and_drop(self, source_locator, target_locator):
        self.logger.info("Dragging element from source {source_locator} to target {target_locator} using {by}")
        source_element = self.driver.find_element(source_locator)
        target_element = self.driver.find_element(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()
    
    def file_upload(self, by, locator, file_path):
        self.logger.info("Uploading file located at {file_path} with locator {locator} using {by}")
        file_input = self.driver.find_element(by, locator)
        file_input.send_keys(file_path)

    def js_scroll_top_of_page(self, driver):
        self.logger.info("Scrolling to the top of the page")
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    
    def js_scroll_bottom_of_page(self, driver):
        self.logger.info("Scrolling to the bottom of the page")
        driver.find_element_by_tag_name('body').send_keys(Keys.END)

    def element_exists(self, by, locator):
        self.logger.info("Checking if element exists with locator {locator} using {by}")
        try:
            self._find_element(by, locator)
            self.logger.info("Element with locator {locator} exists.")
            return True
        except NoSuchElementException:
            self.logger.warning("Element with locator {locator} not found.")
            return False
    
    def element_enabled(self, by, locator):
        try:
            element = self._find_element(by, locator)
            enabled = element.is_enabled()
            if enabled:
                self.logger.info("Element with locator {locator} is enabled.")
            else:
                self.logger.warning("Element with locator {locator} is disabled.")
            return enabled
        except NoSuchElementException:
            self.logger.error("Element with locator {locator} not found.")
            return False
    
    def element_disabled(self, by, locator):
        try:
            element = self._find_element(by, locator)
            disabled = not element.is_enabled()
            if disabled:
                self.logger.info("Element with locator {locator} is disabled.")
            else:
                self.logger.warning("Element with locator {locator} is enabled.")
            return disabled
        except NoSuchElementException:
            self.logger.error("Element with locator {locator} not found.")
            return False
    
    def element_displayed(self, by, locator):
        try:
            element = self._find_element(by, locator)
            displayed = element.is_displayed()
            if displayed:
                self.logger.info("Element with locator {locator} is displayed.")
            else:
                self.logger.warning("Element with locator {locator} is not displayed.")
            return displayed
        except NoSuchElementException:
            self.logger.error("Element with locator {locator} not found.")
            return False
    
    def element_selected(self, by, locator):
        try:
            element = self._find_element(by, locator)
            selected = element.is_selected()
            if selected:
                self.logger.info("Element with locator {locator} is selected.")
            else:
                self.logger.warning("Element with locator {locator} is not selected.")
            return selected
        except NoSuchElementException:
            self.logger.error("Element with locator {locator} not found.")
            return False
    
    def element_clickable(self, by, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
            self.logger.info("Element with locator {locator} is clickable.")
            return True
        except (NoSuchElementException, ElementNotInteractableException):
            self.logger.error("Element with locator {locator} is not clickable.")
            return False