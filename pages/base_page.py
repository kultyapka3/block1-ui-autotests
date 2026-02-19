import allure
from data.data_ui import DEFAULT_TIMEOUT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from typing import Tuple, Optional, Any

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

    @allure.step('Поиск видимых элементов {locator}')
    def wait_for_elements_to_be_present(self, locator: Locator, timeout: Optional[int] = None) -> list[WebElement]:
        timeout = timeout or self.default_timeout

        return WebDriverWait(self.driver, timeout).until(
            ec.presence_of_all_elements_located(locator)
        )

    @allure.step('Поиск элементов {locator}')
    def find_elements(self, locator: Locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

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

    @allure.step('Обновление страницы')
    def refresh_page(self) -> None:
        self.driver.refresh()

    @allure.step('Прокручивание страницы до середины')
    def scroll_page_to_middle(self) -> None:
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight / 2);'
        )

    @allure.step('Разфокусировка с элемента {element}')
    def remove_focus_from_element(self, element: WebElement) -> None:
        self.driver.execute_script('arguments[0].blur();', element)

    @allure.step('Проверка активности элемента {element}')
    def element_is_active(self, element: WebElement) -> bool:
        return self.driver.execute_script(
            'return document.activeElement === arguments[0];', element
        )

    @allure.step('Проверка наличия вертикального скролла')
    def has_vertical_scroll(self) -> bool:
        return self.driver.execute_script(
            'return document.documentElement.scrollHeight > document.documentElement.clientHeight;'
        )

    @allure.step('Прокручивание страницы до конца')
    def scroll_to_bottom(self) -> None:
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    @allure.step('Проверка достижения конца страницы')
    def is_at_bottom(self) -> bool:
        return self.driver.execute_script(
            'return (window.innerHeight + window.scrollY) >= document.body.scrollHeight;'
        )

    # Ленивая инициализация
    def __getattr__(self, name: str) -> Any:
        if name.endswith('_field'):
            locator_name: str = name.replace('_field', '').upper() + '_LOCATOR'

            if hasattr(self, locator_name):
                locator: Locator = getattr(self, locator_name)

                if not hasattr(self, f'_{name}'):
                    setattr(self, f'_{name}', self.find_element(locator))
                return getattr(self, f'_{name}')

        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
