import allure
from data.data_ui import RegistrationTestData
from pages.registration_form_page import RegistrationFormPage
import pytest
from typing import List
from utils.hobby_len_calculator import get_longest_hobby

@allure.suite('U1 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Register Form Page')
@allure.story('Register Form Page: Failed Registration')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('TC05: Регистрация в "Sample Form" с пропущенным полем "Gender"')
@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.successful
@pytest.mark.U1
def test_registration_page_failure(registration_form_page: RegistrationFormPage) -> None:
    registration_form_page.open_sample_form() \
                          .enter_first_name(RegistrationTestData.FIRST_NAME) \
                          .enter_last_name(RegistrationTestData.LAST_NAME) \
                          .enter_email(RegistrationTestData.EMAIL) \
                          .enter_password(RegistrationTestData.PASSWORD) \
                          .select_hobby(RegistrationTestData.HOBBY)

    hobbies: List[str] = registration_form_page.get_hobbies_list()
    about_text: str = get_longest_hobby(hobbies)

    registration_form_page.enter_about_yourself(about_text) \
                          .register()

    error_message: str = registration_form_page.get_error_message()

    with allure.step(f'Проверка сообщения об ошибки регистрации {error_message}'):
        assert error_message, \
            f'Сообщение {error_message} не найдено'
