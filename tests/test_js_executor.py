import allure
from data.data_ui import CUSTOM_TEXT
from pages.sql_main_page import SqlMainPage
import pytest
from selenium.webdriver.remote.webelement import WebElement

@allure.suite('U6 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('SQL Main Page')
@allure.story('SQL Main Page: JS Executor')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('TC09: Проверка работы JavaScriptExecutor')
@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.successful
def test_login_page_valid_credentials_login_success(sql_main_page: SqlMainPage) -> None:
    sql_main_page.enter_login(CUSTOM_TEXT)
    login_field: WebElement = sql_main_page.find_login_field()
    sql_main_page.remove_focus_from_login_field(login_field)

    assert not sql_main_page.is_login_field_active(login_field), \
        f'Фокус должен был быть снят с поля логина'

    vertical_scroll: bool = sql_main_page.has_vertical_scroll()

    if vertical_scroll:
        sql_main_page.scroll_to_bottom()

        assert sql_main_page.is_at_bottom(), \
            f'Страница не прокручена до конца'
    else:
        assert vertical_scroll, \
            f'Страница не имеет вертикальной прокрутки'
