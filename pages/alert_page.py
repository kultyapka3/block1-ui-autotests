import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple

Locator = Tuple[By, str]

class AlertPage(BasePage):
    # Локаторы
    INPUT_ALERT_BUTTON: Locator = (By.XPATH, '//a[text()="Input Alert"]')
    IFRAME_LOCATOR: Locator = (By.XPATH, '//iframe[contains(@src, "input-alert.html")]')
    DEMONSTRATE_ALERT_BUTTON: Locator = (By.XPATH, '//button[contains(., "Click the button to demonstrate the Input box")]')
    ALERT_RESULT: Locator = (By.ID, 'demo')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переключение в iframe')
    def switch_to_iframe(self) -> 'AlertPage':
        iframe: WebElement = self.find_visible_element(self.IFRAME_LOCATOR)
        self.driver.switch_to.frame(iframe)

        return self

    @allure.step('Переключение из iframe')
    def switch_from_iframe(self) -> 'AlertPage':
        self.driver.switch_to.default_content()

        return self

    @allure.step('Переключение на INPUT ALERT')
    def switch_to_input_alert(self) -> 'AlertPage':
        self.click_element(self.INPUT_ALERT_BUTTON)

        return self

    @allure.step('Нажатие на кнопку вызова алерта')
    def demonstrate_alert(self) -> 'AlertPage':
        self.click_element(self.DEMONSTRATE_ALERT_BUTTON)

        return self

    @allure.step('Ввод текста {text} в алерт и подтверждение')
    def complete_alert(self, text: str) -> 'AlertPage':
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

        return self

    @allure.step('Получение результата')
    def get_alert_result(self) -> str:
        return self.find_visible_element(self.ALERT_RESULT).text.strip()
