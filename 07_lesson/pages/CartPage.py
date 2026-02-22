from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CartPage(BasePage):
    """Класс для страницы корзины"""

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def checkout(self):
        """Начать оформление заказа"""
        self.find_clickable_element(self.CHECKOUT_BUTTON).click()