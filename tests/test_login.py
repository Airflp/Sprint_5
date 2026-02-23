from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import MainPage, RegistrationPage, ForgotPasswordPage
from utils.config import BASE_URL
from utils.helpers import login


class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPage.LOGIN_BUTTON).click()

        login(driver)

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.PERSONAL_ACCOUNT)
        )

    def test_login_from_personal_account(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPage.PERSONAL_ACCOUNT).click()

        login(driver)

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.PERSONAL_ACCOUNT)
        )

    def test_login_from_registration_page(self, driver):
        driver.get(f"{BASE_URL}/register")
        driver.find_element(*RegistrationPage.LOGIN_LINK).click()

        login(driver)

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.PERSONAL_ACCOUNT)
        )

    def test_login_from_forgot_password_page(self, driver):
        driver.get(f"{BASE_URL}/forgot-password")
        driver.find_element(*ForgotPasswordPage.LOGIN_LINK).click()

        login(driver)

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.PERSONAL_ACCOUNT)
        )