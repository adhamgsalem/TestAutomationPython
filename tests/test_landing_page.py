import pytest
from pages.landing_page import LandingPage
from utils.browser_setup import get_driver

@pytest.fixture
def navigate_to_url():
    driver = get_driver(browser='safari', headless=True)
    driver.get("https://formy-project.herokuapp.com/")
    yield driver
    driver.quit()
 
def test_logo_is_displayed(navigate_to_url):
    driver = navigate_to_url
    landing_page = LandingPage(driver)
    landing_page.logo_displayed()
