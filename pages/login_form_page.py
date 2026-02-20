import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from typing import Tuple

Locator = Tuple[By, str]

class LoginFormPage(BasePage):
    # Локаторы
    USERNAME_LOGIN_FIELD: Locator = (By.ID, 'username')
    PASSWORD_FIELD: Locator = (By.ID, 'password')
    USERNAME_FIELD: Locator = (By.XPATH, '//div[contains(@class, "formly-field-input")]//input[@required]')
    LOGIN_BUTTON: Locator = (By.XPATH, '//button[@ng-click="Auth.login()"]')
    SUCCESS_MESSAGE: Locator = (By.XPATH, '//p[text()="You\'re logged in!!"]')
    ERROR_MESSAGE: Locator = (By.XPATH, '//div[@ng-if="Auth.error"]')
    LOGOUT_BUTTON: Locator = (By.LINK_TEXT, 'Logout')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввод логина {username_login}')
    def enter_username_login(self, username_login: str) -> 'LoginFormPage':
        self.send_keys_to_element(self.USERNAME_LOGIN_FIELD, username_login)

        return self

    @allure.step('Ввод пароля {password}')
    def enter_password(self, password: str) -> 'LoginFormPage':
        self.send_keys_to_element(self.PASSWORD_FIELD, password)

        return self

    @allure.step('Ввод имени {username}')
    def enter_username(self, username: str) -> 'LoginFormPage':
        self.send_keys_to_element(self.USERNAME_FIELD, username)

        return self

    @allure.step('Получение состояния кнопки "Login"')
    def is_login_button_enabled(self) -> bool:
        return self.find_visible_element(self.LOGIN_BUTTON).is_enabled()

    @allure.step('Нажатие на кнопку "Login"')
    def login(self) -> 'LoginFormPage':
        self.click_element(self.LOGIN_BUTTON)

        return self

    @allure.step('Получение сообщения об успешной авторизации')
    def get_success_message(self) -> str:
        return self.find_visible_element(self.SUCCESS_MESSAGE).text.strip()

    @allure.step('Получение сообщения об ошибке авторизации')
    def get_error_message(self) -> str:
        return self.find_visible_element(self.ERROR_MESSAGE).text.strip()

    @allure.step('Нажатие на кнопку "Logout"')
    def logout(self) -> 'LoginFormPage':
        self.click_element(self.LOGOUT_BUTTON)

        return self

    @allure.step('Получение URL страницы')
    def get_page_url(self) -> str:
        return super().get_current_url()
