from selenium.webdriver.common.by import By
import re
from .BasePage import BasePage


class CheckoutPage(BasePage):
    """Класс для страницы оформления заказа"""

    # Поля формы
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Итоговая информация
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Заполнить форму оформления заказа"""
        self.find_element(self.FIRST_NAME_FIELD).send_keys(first_name)
        self.find_element(self.LAST_NAME_FIELD).send_keys(last_name)
        self.find_element(self.POSTAL_CODE_FIELD).send_keys(postal_code)
        self.find_clickable_element(self.CONTINUE_BUTTON).click()

    def get_total_price(self):
        """Получить итоговую стоимость заказа"""
        total_text = self.find_element(self.TOTAL_LABEL).text
        # Извлекаем число из строки, например из "Total: $58.29"
        match = re.search(r'\$([\d\.]+)', total_text)
        if match:
            return match.group(1)  # Возвращаем "58.29"
        else:
            raise ValueError(f"Не удалось извлечь стоимость из: {total_text}")