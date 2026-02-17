import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from typing import Tuple

# Тип локатора для аннотаций
Locator = Tuple[By, str]

class LifetimeMembershipPage(BasePage):
    # Локатор
    PAGE_TITLE: Locator = (By.XPATH, '//h1[contains(., "LIFETIME MEMBERSHIP CLUB")]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Получение заголовка страницы')
    def get_page_title(self) -> str:
        return self.find_visible_element(self.PAGE_TITLE).text

    @allure.step('Получение URL страницы')
    def get_page_url(self) -> str:
        return super().get_current_url()
