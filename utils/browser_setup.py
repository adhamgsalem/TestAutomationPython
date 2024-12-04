from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.safari.options import Options as SafariOptions


def get_driver(browser='chrome', headless=False, maximized=False):
    if browser == 'chrome':
        chrome_options = ChromeOptions()

        if headless:
            chrome_options.add_argument("--headless")

        if maximized:
            chrome_options.add_argument("--start-maximized")

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

    elif browser == 'firefox':
        firefox_options = FirefoxOptions()

        if headless:
            firefox_options.add_argument("--headless")

        if maximized:
            firefox_options.add_argument("--start-maximized")

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
    
    elif browser == 'safari':
        safari_options = SafariOptions()

        if headless:
            safari_options.add_argument("--headless")

        if maximized:
            safari_options.add_argument("--start-maximized")
        
        service = SafariService()
        driver = webdriver.Safari(service=service, options=safari_options)
    
    else:
        raise ValueError("Unsupported browser: Choose either 'chrome', 'firefox', or 'safari'")

    return driver