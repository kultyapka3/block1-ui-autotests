import allure
from data.data_ui import SQL_COOKIE_LOGIN_URL, COOKIE_FILE_PATH
from data.data_for_login_with_cookies import LoginDataWithCookies
import os
import pytest
from pages.sql_cookie_login_page import SqlCookieLoginPage
from utils.cookie_manager import CookieManager

@allure.suite('U5 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Login Form Page With Cookies')
@allure.story('Login Form Page: Login With Cookies')
class TestLoginWithCookies:
    # Получение режима запуска теста
    def get_run_mode(self, request) -> str:
        return request.config.getoption('--run-mode')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('TC08: Авторизация с использованием cookies')
    @pytest.mark.ui
    @pytest.mark.successful
    @pytest.mark.cookies
    def test_login_with_cookies(self, driver, request) -> None:
        run_mode = self.get_run_mode(request)
        sql_cookie_login_page = SqlCookieLoginPage(driver)

        with allure.step(f'Запуск в режиме: {run_mode}'):
            if run_mode == 'first':
                self._run_first_time(sql_cookie_login_page, driver)
            elif run_mode == 'second':
                self._run_second_time(sql_cookie_login_page, driver)
            else:
                pytest.fail(f'Неизвестный режим запуска: {run_mode}')

    def _run_first_time(self, sql_cookie_login_page: SqlCookieLoginPage, driver) -> None:
        sql_cookie_login_page.open(SQL_COOKIE_LOGIN_URL)

        sql_cookie_login_page.enter_username(LoginDataWithCookies.LOGIN) \
                             .enter_password(LoginDataWithCookies.PASSWORD) \
                             .login()

        username: str = sql_cookie_login_page.get_username(LoginDataWithCookies.USERNAME)

        with allure.step(f'Проверка имени пользователя {username} после входа'):
            assert username == LoginDataWithCookies.USERNAME, \
                f'Имя пользователя {username} не совпадает с {LoginDataWithCookies.USERNAME}'

        with allure.step('Сохранение cookies в файл'):
            CookieManager.save_cookies(driver, COOKIE_FILE_PATH)

        sql_cookie_login_page.logout()

    def _run_second_time(self, sql_cookie_login_page: SqlCookieLoginPage, driver) -> None:
        with allure.step('Проверка наличия файла с cookies'):
            if not os.path.exists(COOKIE_FILE_PATH):
                pytest.skip(
                    'Файл с cookies не найден. Сначала запустите тест в режиме first: '
                    'pytest --run-mode=first tests/test_login_with_cookies.py'
                )

        sql_cookie_login_page.open(SQL_COOKIE_LOGIN_URL)

        with allure.step(f'Добавление Cookies'):
            CookieManager.load_cookies(driver, COOKIE_FILE_PATH)

        username: str = sql_cookie_login_page.get_username(LoginDataWithCookies.USERNAME)

        with allure.step(f'Проверка имени пользователя {username} после входа'):
            assert username == LoginDataWithCookies.USERNAME, \
                f'Имя пользователя {username} не совпадает с {LoginDataWithCookies.USERNAME}'
