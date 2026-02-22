from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import (
    LoginPage,
    MainPage,
    RegistrationPage,
    ForgotPasswordPage
)
from utils.config import BASE_URL, STELLAR_EMAIL, STELLAR_PASSWORD


def login(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located(LoginPage.EMAIL_INPUT)
    ).send_keys(STELLAR_EMAIL)

    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(STELLAR_PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    wait.until(EC.url_changes(f"{BASE_URL}/login"))


def test_login_from_main_page(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPage.LOGIN_BUTTON).click()
    login(driver)


def test_login_from_personal_account(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPage.PERSONAL_ACCOUNT).click()
    login(driver)


def test_login_from_registration_page(driver):
    driver.get(f"{BASE_URL}/register")
    driver.find_element(*RegistrationPage.LOGIN_LINK).click()
    login(driver)


def test_login_from_forgot_password_page(driver):
    driver.get(f"{BASE_URL}/forgot-password")
    driver.find_element(*ForgotPasswordPage.LOGIN_LINK).click()
    login(driver)
