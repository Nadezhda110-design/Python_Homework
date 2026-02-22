from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator, timeout=10):
        """Найти элемент с ожиданием"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )

    def find_clickable_element(self, locator, timeout=10):
        """Найти элемент, доступный для клика"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не доступен для клика"
        )