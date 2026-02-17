import logging
import os
import pytest
from pytest import Session, ExitCode
from selenium import webdriver
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

# Фикстура для веб-драйвера
@pytest.fixture(scope='function')
def driver() -> Generator[WebDriver, None, None]:
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

# Хук для генерации отчетов Allure
@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session: Session, exitstatus: int | ExitCode) -> None:
    # Запускаем только в локальной среде
    if os.getenv('CI'):
        return

    # Если процесс не главный, то не запускаем
    if hasattr(session.config, 'workerinput'):
        return

    allure_results_dir = session.config.getoption('--alluredir')
    # subprocess.Popen(['allure', 'serve', f'{allure_results_dir}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
