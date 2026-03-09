from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    """
    Конструктор класса BasePage.

    :param driver: WebDriver — объект драйвера Selenium.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нахождение элемента с ожиданием")
    def find_element(self, locator, timeout=10):
        """
        Находит элемент с ожиданием 10 секунд

        :param locator: str - поле для ввода данных.
        :param timeout: int - время задержки в секундах.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )

    @allure.step("Нахождение элемента, доступного для клика")
    def find_clickable_element(self, locator, timeout=10):
        """
        Находит элемент, доступный для клика

        :param locator: str - текст на кнопке, которую нужно нажать.
        :param timeout: int - время задержки в секундах.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не доступен для клика"
        )