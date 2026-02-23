from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import RegistrationPage
from utils.config import BASE_URL
from utils.helpers import login
from utils.generators import generate_email, generate_password


class TestRegistration:

    def test_success_registration(self, driver):
        driver.get(f"{BASE_URL}/register")

        email = generate_email()
        password = generate_password()

        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys("Test User")
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        assert "/login" in driver.current_url

    def test_registration_with_short_password(self, driver):
        driver.get(f"{BASE_URL}/register")

        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys("Test User")
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys("test@test.ru")
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys("123")
        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPage.PASSWORD_ERROR)
        )