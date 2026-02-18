import allure
from data.data_ui import DEFAULT_TIMEOUT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from typing import Tuple, Optional

Locator = Tuple[By, str]

class BasePage:
    def __init__(self, driver: WebDriver, default_timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.default_timeout = default_timeout
        self.wait = WebDriverWait(driver, default_timeout)

    @allure.step('Открытие страницы {url}')
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step('Поиск элемента {locator}')
    def find_element(self, locator: Locator, timeout: Optional[int] = None) -> WebElement:
        timeout = timeout or self.default_timeout

        return WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(locator)
        )

    def wait_for_elements_to_be_present(self, locator: Locator, timeout: Optional[int] = None) -> list[WebElement]:
        timeout = timeout or self.default_timeout

        return WebDriverWait(self.driver, timeout).until(
            ec.presence_of_all_elements_located(locator)
        )

    @allure.step('Поиск элементов {locator}')
    def find_elements(self, locator: Locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    @allure.step('Прокручивание страницы до середины')
    def scroll_page_to_middle(self) -> None:
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight / 2);'
        )

    @allure.step('Поиск видимого элемента {locator}')
    def find_visible_element(self, locator: Locator, timeout: Optional[int] = None) -> WebElement:
        timeout = timeout or self.default_timeout

        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator)
        )

    @allure.step('Поиск кликабельного элемента {locator}')
    def find_clickable_element(self, locator: Locator, timeout: Optional[int] = None) -> WebElement:
        timeout = timeout or self.default_timeout

        return WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable(locator)
        )

    @allure.step('Клик по элементу {locator}')
    def click_element(self, locator: Locator) -> None:
        element = self.find_clickable_element(locator)
        element.click()

    @allure.step('Ввод текста {text} в элемент {locator}')
    def send_keys_to_element(self, locator: Locator, text: str) -> None:
        element = self.find_element(locator)

        if element.get_attribute('value'):
            element.clear()

        element.send_keys(text)

    @allure.step('Получение текущего url')
    def get_current_url(self) -> str:
        return self.driver.current_url
