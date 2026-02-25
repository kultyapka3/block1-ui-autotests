import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple

Locator = Tuple[By, str]

class DragNDropPage(BasePage):
    # Локаторы
    IFRAME_LOCATOR: Locator = (By.CSS_SELECTOR, 'div.freme_box > iframe.demo-frame')
    DRAGGABLE_ELEMENT_LOCATOR: Locator = (By.ID, 'draggable')
    DROPPABLE_ELEMENT_LOCATOR: Locator = (By.ID, 'droppable')
    DROPPABLE_TEXT: Locator = (By.CSS_SELECTOR, '#droppable p')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переключение в iframe')
    def switch_to_iframe(self) -> 'DragNDropPage':
        iframe: WebElement = self.find_visible_element(self.IFRAME_LOCATOR)
        self.driver.switch_to.frame(iframe)

        return self

    @allure.step('Переключение из iframe')
    def switch_from_iframe(self) -> 'DragNDropPage':
        self.driver.switch_to.default_content()

        return self

    @allure.step('Перетаскивание элемента')
    def drag_and_drop(self) -> 'DragNDropPage':
        draggable: WebElement = self.find_clickable_element(self.DRAGGABLE_ELEMENT_LOCATOR)
        droppable: WebElement = self.find_clickable_element(self.DROPPABLE_ELEMENT_LOCATOR)

        ActionChains(self.driver) \
            .drag_and_drop(draggable, droppable) \
            .perform()

        return self

    @allure.step('Получение текста из принимающего элемента')
    def get_droppable_text(self) -> str:
        return self.find_visible_element(self.DROPPABLE_TEXT).text.strip()
