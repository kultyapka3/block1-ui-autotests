from typing import Final, NamedTuple, List

# URL'ы
MAIN_PAGE_URL: Final[str] = 'https://www.way2automation.com/'
LIFETIME_MEMBERSHIP_URL: Final[str] = 'https://www.way2automation.com/lifetime-membership-club/'
LOGIN_FORM_URL: Final[str] = 'https://www.way2automation.com/angularjs-protractor/registeration/#/login'
REGISTRATION_FORM_URL: Final[str] = 'https://www.way2automation.com/angularjs-protractor/banking/#/login'

# Таймауты
DEFAULT_TIMEOUT: Final[int] = 10

# Тестовые данные
# Для формы авторизации
class LoginTestData:
    USERNAME_LOGIN: Final[str] = 'angular'
    PASSWORD: Final[str] = 'password'
    USERNAME: Final[str] = 'Igor'

# Для формы авторизации с параметрами
class LoginTestParameterizedData(NamedTuple):
    test_name: str
    username_login: str
    password: str
    username: str
    expected_result: str
    is_button_enabled: bool

# Тестовые данные для авторизации с параметрами
LOGIN_TEST_PARAMETERIZED_DATA: Final[List[LoginTestParameterizedData]] = [
    LoginTestParameterizedData(
        test_name='Валидные учетные данные',
        username_login='angular',
        password='password',
        username='Hero',
        expected_result='success',
        is_button_enabled=True
    ),
    LoginTestParameterizedData(
        test_name='Невалидный логин',
        username_login='invalid_user',
        password='password',
        username='Hero',
        expected_result='error',
        is_button_enabled=True
    ),
    LoginTestParameterizedData(
        test_name='Невалидный пароль',
        username_login='angular',
        password='invalid_pass',
        username='Hero',
        expected_result='error',
        is_button_enabled=True
    ),
    LoginTestParameterizedData(
        test_name='Пустой логин',
        username_login='',
        password='password',
        username='Hero',
        expected_result='error',
        is_button_enabled=False
    ),
    LoginTestParameterizedData(
        test_name='Пустой пароль',
        username_login='angular',
        password='',
        username='Hero',
        expected_result='error',
        is_button_enabled=False
    ),
    LoginTestParameterizedData(
        test_name='Пробелы в логине и пароле',
        username_login='   ',
        password='   ',
        username='Hero',
        expected_result='error',
        is_button_enabled=False
    )
]

# Для формы регистрации
class RegistrationTestData:
    FIRST_NAME: Final[str] = 'Tony'
    LAST_NAME: Final[str] = 'Stark'
    EMAIL: Final[str] = 'tony@stark.com'
    PASSWORD: Final[str] = 'password123'
    HOBBY: Final[str] = 'Sports'
