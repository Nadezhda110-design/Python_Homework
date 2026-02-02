from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    """Простой рабочий MainPage"""

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_name):
        """Простой метод добавления товара"""
        # Находим все товары
        all_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        for item in all_items:
            # Получаем название
            name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
            if name_element.text == product_name:
                # Находим кнопку
                button = item.find_element(By.TAG_NAME, "button")
                button.click()
                print(f"Добавлен товар: {product_name}")
                return

        raise Exception(f"Товар '{product_name}' не найден")

    def go_to_cart(self):
        """Перейти в корзину"""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()