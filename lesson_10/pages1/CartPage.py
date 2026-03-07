from selenium.webdriver.common.by import By
from .BasePage import BasePage
import allure


class CartPage(BasePage):
    """
    Класс для страницы корзины


    """

    CHECKOUT_BUTTON = (By.ID, "checkout")

    @allure.step("Начало оформления заказа")
    def checkout(self):
        """
        Находит элемент,доступный для клика
        """
        self.find_clickable_element(self.CHECKOUT_BUTTON).click()