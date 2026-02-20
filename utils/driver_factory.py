from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IeOptions
from selenium.webdriver.remote.webdriver import WebDriver

class DriverFactory:
    @staticmethod
    def create_driver(
            browser_name: str = 'chrome',
            run_mode: str = 'local',
            grid_url: str = 'http://localhost:4444',
            headless: bool = True,
            page_load_strategy: str = 'eager'
    ) -> WebDriver:
        browser_name = browser_name.lower()
        run_mode = run_mode.lower()

        if browser_name == 'chrome':
            options = ChromeOptions()
            options.page_load_strategy = page_load_strategy

            if headless:
                options.add_argument('--headless=new')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')

            if run_mode == 'local':
                return webdriver.Chrome(options=options)

            elif run_mode == 'grid':
                options.set_capability('browserName', 'chrome')

                return webdriver.Remote(
                    command_executor=grid_url,
                    options=options
                )

        elif browser_name == 'firefox':
            options = FirefoxOptions()
            options.page_load_strategy = page_load_strategy

            if headless:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')

            if run_mode == 'local':
                return webdriver.Firefox(options=options)

            elif run_mode == 'grid':
                options.set_capability('browserName', 'firefox')

                return webdriver.Remote(
                    command_executor=grid_url,
                    options=options
                )

        elif browser_name == 'edge':
            options = EdgeOptions()
            options.page_load_strategy = page_load_strategy

            if headless:
                options.add_argument('--headless=new')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')

            if run_mode == 'local':
                return webdriver.Edge(options=options)

            elif run_mode == 'grid':
                options.set_capability('browserName', 'MicrosoftEdge')

                return webdriver.Remote(
                    command_executor=grid_url,
                    options=options
                )

        elif browser_name == 'ie':
            options = IeOptions()
            options.page_load_strategy = 'normal'

            options.ignore_protected_mode_settings = True
            options.ignore_zoom_level = True
            options.require_window_focus = False
            options.ensure_clean_session = True

            if run_mode == 'local':
                return webdriver.Ie(options=options)

            elif run_mode == 'grid':
                options.set_capability('browserName', 'internet explorer')

                return webdriver.Remote(
                    command_executor=grid_url,
                    options=options
                )

        raise ValueError(f'Неподдерживаемый браузер: {browser_name} или режим запуска: {run_mode}')
