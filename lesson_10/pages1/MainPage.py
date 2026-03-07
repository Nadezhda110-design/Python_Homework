from selenium.webdriver.common.by import By
from .BasePage import BasePage
import  allure

class MainPage(BasePage):
    """
    Конструкто класса Главной страницы магазина
    """

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step
    def add_product_to_cart(self, product_name):
        """
        Находит элемент по названию товара.
        Находит кнопку добавления товара в корзину

        :param: product_name.
        """

        all_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        for item in all_items:

            name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
            if name_element.text == product_name:
                button = item.find_element(By.TAG_NAME, "button")
                button.click()
                print(f"Добавлен товар: {product_name}")
                return

        raise Exception(f"Товар '{product_name}' не найден")

    @allure.step ("Переход на страницу корзины")
    def go_to_cart(self):
        """
        Переходит на страницу корзины

        :return: None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()