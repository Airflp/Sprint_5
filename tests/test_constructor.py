from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import ConstructorPage
from utils.config import BASE_URL


def test_constructor_tabs(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable(ConstructorPage.SAUCES)).click()
    wait.until(EC.element_to_be_clickable(ConstructorPage.FILLINGS)).click()
    wait.until(EC.element_to_be_clickable(ConstructorPage.BUNS)).click()

    assert True
