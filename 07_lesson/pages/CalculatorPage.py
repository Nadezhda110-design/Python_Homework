from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)
        self.DELAY_INPUT = (By.ID, "delay")
        self.SCREEN = (By.CLASS_NAME, "screen")
        self.URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds):
        delay_element = self.driver.find_element(*self.DELAY_INPUT)
        delay_element.clear()
        delay_element.send_keys(str(seconds))
        return self

    def click_number(self, number):
        number_xpath = f"//span[text()='{number}']"
        number_element = self.driver.find_element(By.XPATH, number_xpath)
        number_element.click()
        return self

    def click_operator(self, operator):
        operator_xpath = f"//span[text()='{operator}']"
        operator_element = self.driver.find_element(By.XPATH, operator_xpath)
        operator_element.click()
        return self

    def click_equals(self):
        equals_xpath = "//span[text()='=']"
        equals_element = self.driver.find_element(By.XPATH, equals_xpath)
        equals_element.click()
        return self

    def calculate(self, num1, operator, num2):
        self.click_number(num1)
        self.click_operator(operator)
        self.click_number(num2)
        self.click_equals()
        return self

    def get_screen_text(self):
        screen_element = self.driver.find_element(*self.SCREEN)
        return screen_element.text

    def wait_for_result(self, expected_result, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_result)
        )
        return self
