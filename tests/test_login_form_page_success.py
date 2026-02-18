import allure
from data.data_ui import LoginTestData, LOGIN_FORM_URL
from pages.login_form_page import LoginFormPage
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

@allure.suite('U1 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Login Form Page')
@allure.story('Login Form Page: Successful Login')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('TC04: Авторизация на сайте с валидными данными')
@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.successful
def test_login_page_valid_credentials_login_success(driver: WebDriver) -> None:
    login_form_page: LoginFormPage = LoginFormPage(driver)
    login_form_page.open(LOGIN_FORM_URL)

    login_form_page.enter_username_login(LoginTestData.USERNAME_LOGIN) \
                   .enter_password(LoginTestData.PASSWORD) \
                   .enter_username(LoginTestData.USERNAME) \
                   .login()

    success_message: str = login_form_page.get_success_message()

    with allure.step(f'Проверка сообщения об успешной авторизации {success_message}'):
        assert success_message, \
            f'Сообщение {success_message} не найдено'

    login_form_page.logout()

    page_url: str = login_form_page.get_page_url()

    with allure.step(f'Проверка URL страницы {page_url}'):
        assert page_url == LOGIN_FORM_URL, \
            f'Неверный URL страницы: {page_url}'
