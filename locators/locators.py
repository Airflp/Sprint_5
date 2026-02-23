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
    NAME_INPUT = (
        "xpath",
        "//label[text()='Имя']/following-sibling::input"
    )
    EMAIL_INPUT = (
        "xpath",
        "//label[text()='Email']/following-sibling::input"
    )
    PASSWORD_INPUT = (
        "xpath",
        "//label[text()='Пароль']/following-sibling::input"
    )
    REGISTER_BUTTON = (
        "xpath",
        "//button[text()='Зарегистрироваться']"
    )
    PASSWORD_ERROR = (
        "xpath",
        "//p[text()='Некорректный пароль']"
    )
    LOGIN_LINK = (
        "xpath",
        "//a[text()='Войти']"
    )

class ForgotPasswordPage:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
class ConstructorPage:
    BUNS = ("xpath", "//span[text()='Булки']")
    SAUCES = ("xpath", "//span[text()='Соусы']")
    FILLINGS = ("xpath", "//span[text()='Начинки']")

    # Заголовки секций (по ним проверяем переключение)
    BUNS_HEADER = ("xpath", "//h2[text()='Булки']")
    SAUCES_HEADER = ("xpath", "//h2[text()='Соусы']")
    FILLINGS_HEADER = ("xpath", "//h2[text()='Начинки']")
