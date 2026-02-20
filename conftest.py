import allure
from data.data_ui import MAIN_PAGE_URL, LOGIN_FORM_URL, REGISTRATION_FORM_URL
from datetime import datetime
import logging
import os
from pages.main_page import MainPage
from pages.lifetime_membership_page import LifetimeMembershipPage
from pages.login_form_page import LoginFormPage
from pages.registration_form_page import RegistrationFormPage
from pages.sql_main_page import SqlMainPage
import pytest
from pytest import Session
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
import subprocess
from typing import Generator, Any
from webdriver_manager.chrome import ChromeDriverManager

# Настройка логирования
def pytest_configure() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

# Настройка общего кэша для всех процессов
os.environ['WDM_GLOBAL_CACHE'] = 'true'
os.environ['WDM_LOCAL'] = os.path.join(os.getcwd(), '.wdm_cache')

# Фикстура для предварительной загрузки драйвера
@pytest.fixture(scope='session', autouse=True)
def setup_driver_cache() -> Generator[None, None, None]:
    ChromeDriverManager().install()
    yield

# Фикстура для создания драйвера
@pytest.fixture(scope='function')
def driver() -> Generator[WebDriver, None, None]:
    options: Options = Options()
    options.page_load_strategy = 'eager'

    service: Service = Service(ChromeDriverManager().install())
    driver: WebDriver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()

# Фикстуры для создания страниц
@pytest.fixture
def main_page(driver: WebDriver) -> MainPage:
    page: MainPage = MainPage(driver)
    page.open(MAIN_PAGE_URL)

    return page

@pytest.fixture
def lifetime_membership_page(main_page: MainPage) -> LifetimeMembershipPage:
    return main_page.navigate_to_lifetime_membership()

@pytest.fixture
def login_form_page(driver: WebDriver) -> LoginFormPage:
    page: LoginFormPage = LoginFormPage(driver)
    page.open(LOGIN_FORM_URL)

    return page

@pytest.fixture
def registration_form_page(driver: WebDriver) -> RegistrationFormPage:
    page: RegistrationFormPage = RegistrationFormPage(driver)
    page.open(REGISTRATION_FORM_URL)

    return page

@pytest.fixture
def sql_main_page(driver: WebDriver) -> SqlMainPage:
    page: SqlMainPage = SqlMainPage(driver)

    return page

# Хук для добавления скриншотов в отчеты Allure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Any) -> Generator[None, Any, None]:
    outcome = yield
    report: Any = outcome.get_result()

    if report.when == 'call' and report.outcome == 'failed':
        driver: Any = item.funcargs.get('driver') if hasattr(item, 'funcargs') else None

        if driver:
            screenshot: bytes = driver.get_screenshot_as_png()
            timestamp: str = datetime.now().strftime('%Y.%m.%d_%H:%M:%S')

            allure.attach(
                screenshot,
                name=f'Failed_test_screenshot_{timestamp}',
                attachment_type=allure.attachment_type.PNG
            )

# Добваление кастомной опции
def pytest_addoption(parser: Any) -> None:
    parser.addoption(
        '--run-mode',
        action='store',
        default='first',
        help='Режим запуска: first (обычная авторизация) или second (авторизация через cookies)'
    )

# Хук для генерации отчетов Allure
@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session: Session) -> None:
    # Запускаем только в локальной среде
    if os.getenv('CI'):
        return

    # Если процесс не главный, то не запускаем
    if hasattr(session.config, 'workerinput'):
        return

    allure_results_dir = session.config.getoption('--alluredir')
    # subprocess.Popen(['allure.bat', 'serve', allure_results_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
