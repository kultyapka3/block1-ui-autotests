import allure
from data.data_ui import LoginTestData
from pages.login_form_page import LoginFormPage
import pytest

@allure.suite('U4 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Login Form Page')
@allure.story('Login Form Page: Failure Login Without Username')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('TC07: Падающий тест авторизации с пустым "Username *"')
@pytest.mark.ui
@pytest.mark.failing
@pytest.mark.U4
def test_login_page_failure_without_username(login_form_page: LoginFormPage) -> None:
    login_form_page.enter_username_login(LoginTestData.USERNAME_LOGIN) \
                   .enter_password(LoginTestData.PASSWORD) \
                   .login()

    error_message: str = login_form_page.get_error_message()

    with allure.step(f'Проверка сообщения об ошибке авторизации {error_message}'):
        assert error_message, \
            f'Сообщение {error_message} не найдено'
