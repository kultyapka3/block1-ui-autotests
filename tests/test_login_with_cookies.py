import allure
from data.data_ui import SQL_MAIN_PAGE_URL, AUTH_COOKIE_FILE_PATH
from data.data_for_login_with_cookies import LoginDataWithCookies
import os
import pytest
from pages.sql_main_page import SqlMainPage
from selenium.webdriver.remote.webdriver import WebDriver
from utils.cookie_manager import CookieManager

@allure.suite('U5 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('SQL Main Page Login')
@allure.story('SQL Main Page: Login With Cookies')
class TestLoginWithCookies:
    # Получение режима запуска теста
    def get_run_mode(self, request: pytest.FixtureRequest) -> str:
        return request.config.getoption('--run-mode-cookies')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('TC08: Авторизация с использованием cookies')
    @pytest.mark.ui
    @pytest.mark.successful
    @pytest.mark.cookies
    @pytest.mark.U5
    def test_login_with_cookies(self, driver: WebDriver, sql_main_page: SqlMainPage, request: pytest.FixtureRequest) -> None:
        run_mode: str = self.get_run_mode(request)

        with allure.step(f'Запуск в режиме: {run_mode}'):
            if run_mode == 'first':
                self._run_first_time(sql_main_page, driver)
            elif run_mode == 'second':
                self._run_second_time(sql_main_page, driver)
            else:
                pytest.fail(f'Неизвестный режим запуска: {run_mode}')

    def _run_first_time(self, sql_main_page: SqlMainPage, driver: WebDriver) -> None:
        sql_main_page.open(SQL_MAIN_PAGE_URL)

        sql_main_page.enter_login(LoginDataWithCookies.LOGIN) \
                     .enter_password(LoginDataWithCookies.PASSWORD) \
                     .login()

        username: str = sql_main_page.get_username(LoginDataWithCookies.USERNAME)

        with allure.step(f'Проверка имени пользователя {username} после входа'):
            assert username == LoginDataWithCookies.USERNAME, \
                f'Имя пользователя {username} не совпадает с {LoginDataWithCookies.USERNAME}'

        with allure.step('Сохранение cookies в файл'):
            CookieManager.save_cookies(driver, AUTH_COOKIE_FILE_PATH)

        sql_main_page.logout()

    def _run_second_time(self, sql_main_page: SqlMainPage, driver: WebDriver) -> None:
        with allure.step('Проверка наличия файла с cookies'):
            if not os.path.exists(AUTH_COOKIE_FILE_PATH):
                pytest.skip(
                    'Файл с cookies не найден. Сначала запустите тест в режиме first: '
                    'pytest --run-mode-cookies=first tests/test_login_with_cookies.py'
                )

        sql_main_page.open(SQL_MAIN_PAGE_URL)

        with allure.step(f'Добавление Cookies'):
            CookieManager.load_cookies(driver, AUTH_COOKIE_FILE_PATH)

        username: str = sql_main_page.get_username(LoginDataWithCookies.USERNAME)

        with allure.step(f'Проверка имени пользователя {username} после входа'):
            assert username == LoginDataWithCookies.USERNAME, \
                f'Имя пользователя {username} не совпадает с {LoginDataWithCookies.USERNAME}'
