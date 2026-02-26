import allure
from data.data_ui import CUSTOM_ALERT_TEXT
from pages.alert_page import AlertPage
import pytest

@allure.suite('U12 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Alert Page')
@allure.story('Alert Page: Input Alert')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('TC13: Проверка работы с Alert')
@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.successful
@pytest.mark.U12
def test_tabs(alert_page: AlertPage) -> None:
    alert_page.switch_to_input_alert() \
              .switch_to_iframe() \
              .demonstrate_alert() \
              .complete_alert(CUSTOM_ALERT_TEXT)

    alert_result = alert_page.get_alert_result()

    with allure.step(f'Проверка результата {alert_result}'):
        assert CUSTOM_ALERT_TEXT in alert_result, \
            f'{CUSTOM_ALERT_TEXT} должен быть в {alert_result}'

    alert_page.switch_from_iframe()
