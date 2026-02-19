import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from typing import Tuple

Locator = Tuple[By, str]

class SqlCookieLoginPage(BasePage):
    # Локаторы
    USERNAME_FIELD: Locator = (By.NAME, 'login')
    PASSWORD_FIELD: Locator = (By.NAME, 'psw')
    LOGIN_BUTTON: Locator = (By.XPATH, '//input[@value="Вход"]')
    LOGOUT_BUTTON: Locator = (By.XPATH, '//img[@title="Выход..."]')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url: str) -> None:
        super().open(url)

    @allure.step('Ввод логина {username}')
    def enter_username(self, username: str) -> 'SqlCookieLoginPage':
        self.send_keys_to_element(self.USERNAME_FIELD, username)

        return self

    @allure.step('Ввод пароля {password}')
    def enter_password(self, password: str) -> 'SqlCookieLoginPage':
        self.send_keys_to_element(self.PASSWORD_FIELD, password)

        return self

    @allure.step('Нажатие на кнопку "Вход"')
    def login(self) -> 'SqlCookieLoginPage':
        self.click_element(self.LOGIN_BUTTON)

        return self

    @allure.step('Получение имени пользователя')
    def get_username(self, username: str) -> str:
        # Динамически определяем локатор для имени пользователя, заданного в data_for_login_with_cookies.py
        username_locator: Locator = (By.XPATH, f'//a[text()="{username}"]')

        return self.find_visible_element(username_locator).text.strip()

    @allure.step('Нажатие на кнопку выхода "замок"')
    def logout(self) -> 'SqlCookieLoginPage':
        self.click_element(self.LOGOUT_BUTTON)

        return self
