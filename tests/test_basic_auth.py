import allure
from data.data_ui import AuthTestData, AUTH_PAGE_URL
from pages.basic_auth_page import BasicAuthPage
import pytest
from utils.url_generator_for_basic_auth import generate_url

@allure.suite('U13 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Basic Auth Page')
@allure.story('Basic Auth Page: Auth')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('TC14: Проверка работы с Basic Auth')
@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.successful
@pytest.mark.U13
def test_basic_auth(basic_auth_page: BasicAuthPage) -> None:
    login, password = AuthTestData.LOGIN, AuthTestData.PASSWORD
    basic_auth_page.open(generate_url(AUTH_PAGE_URL, login, password))
    basic_auth_page.display_image()

    image_src: str = basic_auth_page.is_authenticated_image_displayed()

    with allure.step(f'Проверка, что изображение получило правильный атрибут src: {image_src}'):
        assert f'{login}:{password}' in image_src, \
            f'Изображение не имеет правильного src: {image_src}'
