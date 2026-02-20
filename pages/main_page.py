import allure
from pages.base_page import BasePage
from pages.lifetime_membership_page import LifetimeMembershipPage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from typing import Tuple

Locator = Tuple[By, str]

class MainPage(BasePage):
    # Локаторы
    HEADER_CONTAINER: Locator = (By.CSS_SELECTOR, 'header.site-header')
    PHONE_NUMBERS: Locator = (By.XPATH, '//header//a[contains(@href, "tel:")]')
    NAVIGATION_MENU: Locator = (By.CSS_SELECTOR, '.main-header-bar')
    ALL_COURSES_MENU: Locator = (By.LINK_TEXT, 'All Courses')
    LIFETIME_MEMBERSHIP_LINK: Locator = (By.XPATH, '//a[contains(@href, "lifetime-membership")]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Проверка видимости хедера')
    def is_header_visible(self) -> bool:
        return self.find_visible_element(self.HEADER_CONTAINER).is_displayed()

    @allure.step('Получение номера телефона из хедера')
    def get_phone_number(self) -> str:
        phone_element: WebElement = self.find_visible_element(self.PHONE_NUMBERS)
        phone_text: str = phone_element.text.strip()

        return phone_text.replace(' ', '').replace('-', '')

    @allure.step('Проверка фиксации меню при прокрутке')
    def is_navigation_sticky(self) -> bool:
        self.scroll_page_to_middle()

        return self.find_visible_element(self.NAVIGATION_MENU).is_displayed()

    @allure.step('Переход на страницу Lifetime membership')
    def navigate_to_lifetime_membership(self) -> 'LifetimeMembershipPage':
        self.find_clickable_element(self.ALL_COURSES_MENU).click()
        self.find_visible_element(self.LIFETIME_MEMBERSHIP_LINK)
        self.find_clickable_element(self.LIFETIME_MEMBERSHIP_LINK).click()

        return LifetimeMembershipPage(self.driver)
