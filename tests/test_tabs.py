import allure
from pages.frames_and_windows_page import FramesAndWindowsPage
import pytest

@allure.suite('U11 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Frames and Windows Page')
@allure.story('Frames and Windows Page: Tabs')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('TC12: Проверка работы с несколькими вкладками')
@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.successful
@pytest.mark.U11
def test_tabs(frames_and_windows_page: FramesAndWindowsPage) -> None:
    frames_and_windows_page.switch_to_iframe()

    original_tab = frames_and_windows_page.get_current_handle()

    frames_and_windows_page.open_new_tab() \
                           .switch_to_new_tab(original_tab)

    frames_and_windows_page.open_new_tab()

    tab_count = frames_and_windows_page.get_tab_count()

    with allure.step('Проверка, что открыты 3 вкладки'):
        assert tab_count == 3, \
            f'Количество вкладок равно {tab_count}, а не 3'

    frames_and_windows_page.close_all_tabs_except_original(original_tab) \
                           .switch_to_original_tab(original_tab) \
                           .switch_from_iframe()
