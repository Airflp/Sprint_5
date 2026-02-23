import random
import string


def generate_email():
    return (
        "test_user_"
        + "".join(random.choices(string.digits, k=6))
        + "@yandex.ru"
    )


def generate_password():
    return "".join(random.choices(string.ascii_letters + string.digits, k=8))