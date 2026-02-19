from selenium.webdriver.common.by import By


class LoginPage:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")


class MainPage:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")


class AccountPage:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")


class RegistrationPage:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class ForgotPasswordPage:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
class ConstructorPage:
    BUNS = (By.XPATH, "//span[text()='Булки']")
    SAUCES = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS = (By.XPATH, "//span[text()='Начинки']")

