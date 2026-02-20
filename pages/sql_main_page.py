import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple

Locator = Tuple[By, str]

class SqlMainPage(BasePage):
    # Локаторы
    LOGIN_FIELD: Locator = (By.NAME, 'login')
    PASSWORD_FIELD: Locator = (By.NAME, 'psw')
    LOGIN_BUTTON: Locator = (By.XPATH, '//input[@value="Вход"]')
    LOGOUT_BUTTON: Locator = (By.XPATH, '//img[@title="Выход..."]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввод логина {login}')
    def enter_login(self, login: str) -> 'SqlMainPage':
        self.send_keys_to_element(self.LOGIN_FIELD, login)

        return self

    @allure.step('Ввод пароля {password}')
    def enter_password(self, password: str) -> 'SqlMainPage':
        self.send_keys_to_element(self.PASSWORD_FIELD, password)

        return self

    @allure.step('Нажатие на кнопку "Вход"')
    def login(self) -> 'SqlMainPage':
        self.click_element(self.LOGIN_BUTTON)

        return self

    @allure.step('Получение имени пользователя')
    def get_username(self, username: str) -> str:
        # Динамически определяем локатор для имени пользователя, заданного в data_for_login_with_cookies.py
        username_locator: Locator = (By.XPATH, f'//a[text()="{username}"]')

        return self.find_visible_element(username_locator).text.strip()

    @allure.step('Нажатие на кнопку выхода "замок"')
    def logout(self) -> 'SqlMainPage':
        self.click_element(self.LOGOUT_BUTTON)

        return self

    @allure.step('Разфокусировка с поля ввода логина')
    def remove_focus_from_login_field(self, element: WebElement) -> 'SqlMainPage':
        self.remove_focus_from_element(element)

        return self

    @allure.step('Поиск поля ввода логина')
    def find_login_field(self) -> WebElement:
        return self.find_visible_element(self.LOGIN_FIELD)

    @allure.step('Проверка активности поля ввода логина')
    def is_login_field_active(self, element: WebElement) -> bool:
        return self.element_is_active(element)
