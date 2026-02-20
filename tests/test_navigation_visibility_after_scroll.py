import allure
from pages.main_page import MainPage
import pytest

@allure.suite('U1 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Main Page')
@allure.story('Main Page: Navigation Sticky')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('TC02: Фиксация меню навигации при прокрутке страницы')
@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.successful
def test_main_page_navigation_menu_visibility_after_scroll(main_page: MainPage) -> None:
    assert main_page.is_navigation_sticky(), \
        'Меню навигации не фиксируется при прокрутке страницы'
