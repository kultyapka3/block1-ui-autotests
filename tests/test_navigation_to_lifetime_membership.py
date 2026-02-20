import allure
from data.data_ui import LIFETIME_MEMBERSHIP_URL
from pages.lifetime_membership_page import LifetimeMembershipPage
import pytest

@allure.suite('U1 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Main Page Navigation To Lifetime Membership Page')
@allure.story('Main Page: Navigation To Lifetime Membership Page')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('TC03: Переход по меню навигации на страницу Lifetime Membership')
@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.successful
def test_main_page_navigation_to_lifetime_membership(lifetime_membership_page: LifetimeMembershipPage) -> None:
    page_title: str = lifetime_membership_page.get_page_title()

    with allure.step(f'Проверка заголовка страницы {page_title}'):
        assert 'MEMBERSHIP' in page_title, \
            f'Неверный заголовок страницы Lifetime Membership: {page_title}'

    page_url: str = lifetime_membership_page.get_page_url()

    with allure.step(f'Проверка URL страницы {page_url}'):
        assert page_url == LIFETIME_MEMBERSHIP_URL, \
            f'Неверный URL страницы Lifetime Membership: {page_url}'
