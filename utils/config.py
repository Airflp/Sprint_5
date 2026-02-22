import os

BASE_URL = "https://stellarburgers.education-services.ru"

STELLAR_EMAIL = os.getenv("STELLAR_EMAIL")
STELLAR_PASSWORD = os.getenv("STELLAR_PASSWORD")

if not STELLAR_EMAIL or not STELLAR_PASSWORD:
    raise RuntimeError(
        "Не заданы переменные окружения STELLAR_EMAIL / STELLAR_PASSWORD"
    )
