from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalculatorPage:
    def __init__(self, driver):
        """
        Конструктор класса CalculatorPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)
        self.DELAY_INPUT = (By.ID, "delay")
        self.SCREEN = (By.CLASS_NAME, "screen")
        self.URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.

        :return: WebDriver
        """
        self.driver.get(self.URL)
        return self

    @allure.step("Установка задержки {delay} секунд")
    def set_delay(self, seconds: int):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param seconds: int — время задержки в секундах.
        """

        delay_element = self.driver.find_element(*self.DELAY_INPUT)
        delay_element.clear()
        delay_element.send_keys(str(seconds))
        return self

    @allure.step("Нажатие кнопки '{number}'")
    def click_number(self, number):
        """
        Нажимает на кнопку калькулятора c цифрой.

        :param number: str — текст на кнопке, которую нужно нажать.
        """
        number_xpath = f"//span[text()='{number}']"
        number_element = self.driver.find_element(By.XPATH, number_xpath)
        number_element.click()
        return self

    @allure.step("Нажатие кнопки '{operator}'")
    def click_operator(self, operator):
        """
        Нажимает на кнопку калькулятора с арифметическим действием (+,-,х,÷).

        :param operator: str — текст на кнопке, которую нужно нажать.
        """
        operator_xpath = f"//span[text()='{operator}']"
        operator_element = self.driver.find_element(By.XPATH, operator_xpath)
        operator_element.click()
        return self

    @allure.step("Нажатие кнопки '='")
    def click_equals(self):
        """
        Нажимает на кнопку калькулятора =.
        """
        equals_xpath = "//span[text()='=']"
        equals_element = self.driver.find_element(By.XPATH, equals_xpath)
        equals_element.click()
        return self

    @allure.step("Ожидание результата '{expected_result}'")
    def wait_for_result(self, expected_result, timeout=50):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        :param expected_result: str — ожидаемый результат.
        :param timeout: int — время задержки в секундах.
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_result)
        )
        return self

    @allure.step("Получение результата с экрана калькулятора")
    def get_screen_text(self):
        """
        Получает текст с результатом
        :return: str — текст результата на экране калькулятора.
        """
        screen_element = self.driver.find_element(*self.SCREEN)
        return screen_element.text

