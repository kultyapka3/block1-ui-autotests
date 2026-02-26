import allure
from pages.drag_n_drop_page import DragNDropPage
import pytest

@allure.suite('U10 test-cases')
@allure.epic('Block1: UI Auto-tests')
@allure.feature('Drag N Drop Page')
@allure.story('Drag N Drop Page: Element dropping')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('TC11: Проверка работы drag and drop')
@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.successful
@pytest.mark.U10
def test_drag_and_drop(drag_n_drop_page: DragNDropPage) -> None:
    drag_n_drop_page.switch_to_iframe() \
                    .drag_and_drop()

    droppable_text: str = drag_n_drop_page.get_droppable_text()

    with allure.step(f'Проверка текста принимающего элемента {droppable_text}'):
        assert droppable_text == 'Dropped!', \
            f'Текст принимающего элемента {droppable_text} не соответствует ожидаемому'

    drag_n_drop_page.switch_from_iframe()
