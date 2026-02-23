import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import ConstructorPage
from utils.config import BASE_URL


class TestConstructor:

    @pytest.mark.parametrize(
        "tab, active_tab",
        [
            (ConstructorPage.SAUCES, ConstructorPage.ACTIVE_TAB_SAUCES),
            (ConstructorPage.FILLINGS, ConstructorPage.ACTIVE_TAB_FILLINGS),
            (ConstructorPage.BUNS, ConstructorPage.ACTIVE_TAB_BUNS),
        ]
    )
    def test_constructor_tabs(self, driver, tab, active_tab):
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(tab)).click()

        assert wait.until(
            EC.visibility_of_element_located(active_tab)
        )