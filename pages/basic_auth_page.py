import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple

Locator = Tuple[By, str]

class BasicAuthPage(BasePage):
    # Локаторы
    DISPLAY_IMAGE_BUTTON: Locator = (By.ID, 'displayImage')
    AUTHENTICATED_IMAGE: Locator = (By.ID, 'downloadImg')
    AUTH_BODY_LOCATOR: Locator = (By.TAG_NAME, 'body')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажатие на кнопку DISPLAY IMAGE')
    def display_image(self) -> 'BasicAuthPage':
        self.click_element(self.DISPLAY_IMAGE_BUTTON)

        return self

    @allure.step('Получение атрибута src из изображения')
    def is_authenticated_image_displayed(self) -> str:
        image: WebElement = self.find_visible_element(self.AUTHENTICATED_IMAGE)

        return image.get_attribute('src')
