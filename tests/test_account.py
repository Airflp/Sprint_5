from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import LoginPage, MainPage, AccountPage
from utils.config import BASE_URL, STELLAR_EMAIL, STELLAR_PASSWORD


def test_go_to_personal_account(driver):
    driver.get(f"{BASE_URL}/login")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPage.EMAIL_INPUT)
    ).send_keys(STELLAR_EMAIL)

    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(STELLAR_PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPage.PERSONAL_ACCOUNT)
    ).click()

    assert "/account" in driver.current_url


def test_logout_from_account(driver):
    driver.get(f"{BASE_URL}/login")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPage.EMAIL_INPUT)
    ).send_keys(STELLAR_EMAIL)

    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(STELLAR_PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPage.PERSONAL_ACCOUNT)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(AccountPage.LOGOUT_BUTTON)
    ).click()

    # Ждём, пока реально выйдет
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

    assert "/login" in driver.current_url
