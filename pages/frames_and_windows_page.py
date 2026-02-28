import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple

Locator = Tuple[By, str]

class FramesAndWindowsPage(BasePage):
    # Локаторы
    IFRAME_LOCATOR: Locator = (By.XPATH, '//iframe[contains(@src, "frames-windows/defult1.html")]')
    NEW_TAB_LINK: Locator = (By.LINK_TEXT, 'New Browser Tab')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переключение в iframe')
    def switch_to_iframe(self) -> 'FramesAndWindowsPage':
        iframe: WebElement = self.find_visible_element(self.IFRAME_LOCATOR)
        self.driver.switch_to.frame(iframe)

        return self

    @allure.step('Переключение из iframe')
    def switch_from_iframe(self) -> 'FramesAndWindowsPage':
        self.driver.switch_to.default_content()

        return self

    @allure.step('Открытие новой вкладки')
    def open_new_tab(self) -> 'FramesAndWindowsPage':
        self.click_element(self.NEW_TAB_LINK)

        return self

    @allure.step('Сохранение дискритора текущей вкладки')
    def get_current_handle(self) -> str:
        return self.get_current_window_handle().strip()
