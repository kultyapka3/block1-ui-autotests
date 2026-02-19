import json
import os
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Any, Dict, List

class CookieManager:
    @staticmethod
    def save_cookies(driver: WebDriver, file_path: str) -> None:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w') as file:
            json.dump(driver.get_cookies(), file)

    @staticmethod
    def load_cookies(driver: WebDriver, file_path: str) -> None:
        driver.delete_all_cookies()

        with open(file_path, 'r') as file:
            cookies: List[Dict[str, Any]] = json.load(file)

            for cookie in cookies:
                driver.add_cookie(cookie)

        driver.refresh()
