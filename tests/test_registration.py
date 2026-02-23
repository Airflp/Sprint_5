from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import RegistrationPage
from utils.config import BASE_URL
from utils.generators import generate_email, generate_password


class TestRegistration:
    def test_success_registration(self, driver):
        driver.get(f"{BASE_URL}/register")
        wait = WebDriverWait(driver, 10)

        name_input = wait.until(
            EC.presence_of_element_located(RegistrationPage.NAME_INPUT)
        )

        # 🔽 КЛЮЧЕВОЙ МОМЕНТ — скролл
        driver.execute_script("arguments[0].scrollIntoView(true);", name_input)

        name_input.send_keys("Test User")
        driver.find_element(
            *RegistrationPage.EMAIL_INPUT
        ).send_keys(generate_email())

        driver.find_element(
            *RegistrationPage.PASSWORD_INPUT
        ).send_keys(generate_password())

        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()

        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    def test_registration_with_short_password(self, driver):
        driver.get(f"{BASE_URL}/register")
        wait = WebDriverWait(driver, 10)

        name_input = wait.until(
            EC.presence_of_element_located(RegistrationPage.NAME_INPUT)
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", name_input)

        name_input.send_keys("Test User")
        driver.find_element(
            *RegistrationPage.EMAIL_INPUT
        ).send_keys(generate_email())

        driver.find_element(
            *RegistrationPage.PASSWORD_INPUT
        ).send_keys("12345")

        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()

        assert wait.until(
            EC.visibility_of_element_located(RegistrationPage.PASSWORD_ERROR)
        )