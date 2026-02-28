import allure
from data.data_ui import LoginTestData
from pages.login_form_page import LoginFormPage
import pytest

@allure.suite('U4 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Login Form Page')
@allure.story('Login Form Page: Search For A Non-Existent Element')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('TC08: Падающий тест авторизации с отсутствующим элементом страницы')
@pytest.mark.ui
@pytest.mark.failing
@pytest.mark.U4
def test_login_page_failure_search_non_existent_element(login_form_page: LoginFormPage) -> None:
    login_form_page.enter_username_login(LoginTestData.USERNAME_LOGIN) \
                   .enter_password(LoginTestData.PASSWORD) \
                   .enter_username(LoginTestData.USERNAME) \
                   .login()

    error_message: str = login_form_page.get_error_message()

    with allure.step(f'Проверка сообщения об ошибке авторизации {error_message}'):
        assert error_message, \
            f'Сообщение {error_message} не найдено'

    login_form_page.logout()
