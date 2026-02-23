import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import ConstructorPage
from utils.config import BASE_URL


class TestConstructor:
    def test_buns_tab_is_active_by_default(self, driver):
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)
        assert wait.until(
            EC.visibility_of_element_located(ConstructorPage.BUNS_HEADER)
        )

    @pytest.mark.parametrize(
        "tab, header",
        [
            (ConstructorPage.SAUCES, ConstructorPage.SAUCES_HEADER),
            (ConstructorPage.FILLINGS, ConstructorPage.FILLINGS_HEADER),
        ],
    )
    def test_constructor_tabs_switching(self, driver, tab, header):
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(tab)).click()

        assert wait.until(EC.visibility_of_element_located(header))