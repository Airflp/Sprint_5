from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import LoginPage
from utils.config import BASE_URL, STELLAR_EMAIL, STELLAR_PASSWORD


def login(driver):
    wait = WebDriverWait(driver, 10)

    driver.get(f"{BASE_URL}/login")

    wait.until(
        EC.visibility_of_element_located(LoginPage.EMAIL_INPUT)
    ).send_keys(STELLAR_EMAIL)

    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(STELLAR_PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    wait.until(EC.url_contains("/"))