import allure
from data import data_ui
from pages.main_page import MainPage
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

@allure.suite('U1 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Main Page')
@allure.story('Main Page: Navigation Sticky')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('TC02: Фиксация меню навигации при прокрутке страницы')
@pytest.mark.ui
@pytest.mark.positive
def test_main_page_navigation_menu_visibility_after_scroll(driver: WebDriver) -> None:
    main_page: MainPage = MainPage(driver)
    main_page.open(data_ui.MAIN_PAGE_URL)

    assert main_page.is_navigation_sticky(), \
        'Меню навигации не фиксируется при прокрутке страницы'
