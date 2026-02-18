import allure
from data import data_ui
from pages.main_page import MainPage
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

@allure.suite('U1 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Main Page')
@allure.story('Main Page: Header Visibility')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('TC01: Отображение хедера с контактной информацией на главной странице')
@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.successful
def test_main_page_header_contact_info_is_visible(driver: WebDriver) -> None:
    main_page: MainPage = MainPage(driver)
    main_page.open(data_ui.MAIN_PAGE_URL)

    assert main_page.is_header_visible(), \
        'Хедер с контактной информацией не отображается'

    phone_number: str = main_page.get_phone_number()

    with allure.step(f'Проверка номера {phone_number}'):
        assert phone_number, \
            f'Номер телефона {phone_number} не отображается'
