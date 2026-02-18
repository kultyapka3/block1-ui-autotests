import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple, List

Locator = Tuple[By, str]

class RegistrationFormPage(BasePage):
    # Локаторы
    SAMPLE_FORM_BUTTON: Locator = (By.LINK_TEXT, 'Sample Form')
    FIRST_NAME_FIELD: Locator = (By.ID, 'firstName')
    LAST_NAME_FIELD: Locator = (By.ID, 'lastName')
    EMAIL_FIELD: Locator = (By.ID, 'email')
    PASSWORD_FIELD: Locator = (By.ID, 'password')
    HOBBIES_LABELS: Locator = (By.CSS_SELECTOR, 'div.checkbox-group label')
    ABOUT_YOURSELF_FIELD: Locator = (By.ID, 'about')
    REGISTER_BUTTON: Locator = (By.CSS_SELECTOR, 'button[type="submit"]')
    ERROR_MESSAGE: Locator = (By.ID, 'errorMessage')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url: str) -> None:
        super().open(url)

    @allure.step('Открытие формы регистрации "Sample Form"')
    def open_sample_form(self) -> 'RegistrationFormPage':
        self.click_element(self.SAMPLE_FORM_BUTTON)

        return self

    @allure.step('Ввод имени {first_name}')
    def enter_first_name(self, first_name: str) -> 'RegistrationFormPage':
        self.send_keys_to_element(self.FIRST_NAME_FIELD, first_name)

        return self

    @allure.step('Ввод фамилии {last_name}')
    def enter_last_name(self, last_name: str) -> 'RegistrationFormPage':
        self.send_keys_to_element(self.LAST_NAME_FIELD, last_name)

        return self

    @allure.step('Ввод email {email}')
    def enter_email(self, email: str) -> 'RegistrationFormPage':
        self.send_keys_to_element(self.EMAIL_FIELD, email)

        return self

    @allure.step('Ввод пароля {password}')
    def enter_password(self, password: str) -> 'RegistrationFormPage':
        self.send_keys_to_element(self.PASSWORD_FIELD, password)

        return self

    @allure.step('Выбор хобби')
    def select_hobby(self, hobby: str) -> 'RegistrationFormPage':
        # Для динамического выбора хобби
        hobby_locator: Locator = (By.CSS_SELECTOR, f'input[name="hobbies"][value="{hobby}"]')
        self.click_element(hobby_locator)

        return self

    @allure.step('Получение списка хобби')
    def get_hobbies_list(self) -> List[str]:
        self.wait_for_elements_to_be_present(self.HOBBIES_LABELS)
        hobbies_labels: List[WebElement] = self.find_elements(self.HOBBIES_LABELS)
        hobbies: List[str] = []

        for label in hobbies_labels:
            label_text = label.text.strip()

            if label_text:
                hobbies.append(label_text)

        return hobbies

    @allure.step('Ввод информации о себе {about}')
    def enter_about_yourself(self, about: str) -> 'RegistrationFormPage':
        self.send_keys_to_element(self.ABOUT_YOURSELF_FIELD, about)

        return self

    @allure.step('Нажатие на кнопку "Register"')
    def register(self) -> 'RegistrationFormPage':
        self.click_element(self.REGISTER_BUTTON)

        return self

    @allure.step('Получение сообщения об ошибке')
    def get_error_message(self) -> str:
        return self.find_visible_element(self.ERROR_MESSAGE).text.strip()
