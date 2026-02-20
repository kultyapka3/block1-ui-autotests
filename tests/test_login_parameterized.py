import allure
from data.data_ui import LOGIN_TEST_PARAMETERIZED_DATA, LoginTestParameterizedData
from pages.login_form_page import LoginFormPage
import pytest

@allure.suite('U3 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Login Form Page')
@allure.story('Login Form Page: Parameterized Login')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('TC06: Параметризованная авторизация на сайте')
@pytest.mark.ui
@pytest.mark.parameterized
@pytest.mark.successful
@pytest.mark.parametrize('test_data', LOGIN_TEST_PARAMETERIZED_DATA, ids=[data.test_name for data in LOGIN_TEST_PARAMETERIZED_DATA])
def test_login_with_different_credentials(login_form_page: LoginFormPage, test_data: LoginTestParameterizedData) -> None:
    login_form_page.enter_username_login(test_data.username_login) \
                   .enter_password(test_data.password) \
                   .enter_username(test_data.username)

    login_button_state: bool = login_form_page.is_login_button_enabled()
    expected_login_button_state: bool = test_data.is_button_enabled

    with allure.step(f'Проверка состояния кнопки авторизации {login_button_state}'):
        assert login_button_state == expected_login_button_state, \
            f'Ожидаемое состояние кнопки авторизации {expected_login_button_state}'

    if test_data.is_button_enabled:
        login_form_page.login()

        if test_data.expected_result == 'success':
            success_message: str = login_form_page.get_success_message()

            with allure.step(f'Проверка сообщения об успешной авторизации {success_message}'):
                assert success_message, \
                    f'Сообщение об успехе {success_message} не найдено'

            login_form_page.logout()
        else:
            error_message: str = login_form_page.get_error_message()

            with allure.step(f'Проверка сообщения об ошибке {error_message}'):
                assert error_message, \
                    f'Сообщение об ошибке {error_message} не найдено'
