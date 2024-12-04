from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logo = "//a[@id='logo']"
        self.form_link = "//a[normalize-space()='Form']"
        self.components_dropdown = "//a[@id='navbarDropdownMenuLink']"
        self.autocomplete_option = "//a[@class='dropdown-item'][normalize-space()='Autocomplete']"
        self.buttons_option = "//a[@class='dropdown-item'][normalize-space()='Buttons']"
        self.checkbox_option = "//a[@class='dropdown-item'][normalize-space()='Checkbox']"
        self.datepicker_option = "//a[@class='dropdown-item'][normalize-space()='Datepicker']"
        self.drag_option = "//a[@class='dropdown-item'][normalize-space()='Drag and Drop']"
        self.dropdown_option = "//a[@class='dropdown-item'][normalize-space()='Dropdown']"
        self.enable_disable_option = "//a[@class='dropdown-item'][normalize-space()='Enabled and disabled elements']"
        self.upload_option = "//a[@class='dropdown-item'][normalize-space()='File Upload']"
        self.key_mouse_option = "//a[@class='dropdown-item'][normalize-space()='Key and Mouse Press']"
        self.modal_option = "//a[@class='dropdown-item'][normalize-space()='Modal']"
        self.scroll_option = "//a[@class='dropdown-item'][normalize-space()='Page Scroll']"
        self.radio_button_option = "//a[@class='dropdown-item'][normalize-space()='Radio Button']"
        self.switch_window_option = "//a[@class='dropdown-item'][normalize-space()='Switch Window']"
        self.web_form_option = "//a[@class='dropdown-item'][normalize-space()='Complete Web Form']"
        self.error_message = "error"

    def logo_displayed(self):
        self.wait_for_element(By.XPATH, self.logo)

    def get_error_message(self):
        return self.driver.find_element(self.error_message).text
