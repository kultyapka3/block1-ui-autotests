import allure
from datetime import datetime
import logging
import os
import pytest
from pytest import Session
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
import subprocess
from typing import Generator
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
    options = Options()
    options.page_load_strategy = 'eager'

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()

# Хук для добавления скриншотов в отчеты Allure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.outcome == 'failed':
        driver = item.funcargs.get('driver') if hasattr(item, 'funcargs') else None

        if driver:
            screenshot = driver.get_screenshot_as_png()
            timestamp = datetime.now().strftime('%Y.%m.%d_%H:%M:%S')

            allure.attach(
                screenshot,
                name=f'Failed_test_screenshot_{timestamp}',
                attachment_type=allure.attachment_type.PNG
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
    # subprocess.Popen(['allure', 'serve', f'{allure_results_dir}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
