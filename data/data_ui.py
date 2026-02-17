from typing import Final

# URL'ы
MAIN_PAGE_URL: Final[str] = 'https://www.way2automation.com/'
LIFETIME_MEMBERSHIP_URL: Final[str] = 'https://www.way2automation.com/lifetime-membership-club/'
LOGIN_FORM_URL: Final[str] = 'https://www.way2automation.com/angularjs-protractor/registeration/#/login'
REGISTRATION_FORM_URL: Final[str] = 'https://www.way2automation.com/angularjs-protractor/banking/#/login'

# Таймауты
DEFAULT_TIMEOUT: Final[int] = 10

# Тестовые данные
# Для формы авторизации
class TestLoginData:
    USERNAME: Final[str] = 'angular'
    PASSWORD: Final[str] = 'password'

# Для формы регистрации
class TestRegistrationData:
    FIRST_NAME: Final[str] = 'Tony'
    LAST_NAME: Final[str] = 'Stark'
    EMAIL: Final[str] = 'tony@stark.com'
    PASSWORD: Final[str] = 'password123'