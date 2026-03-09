from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BasePage import BasePage
import allure


class LoginPage(BasePage):
    """
    Класс для страницы авторизации
    """

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step ("Авторизация на странице магазина, используя {username}, {password}")
    def authorize(self, username, password):
        """
        Авторизуется под указанным пользователем

        :param username: str - имя пользвателя.
        :param password: str - пароль пользователя.
        Нажимает кнопку LOGIN_BUTTON.
        Ждет перехода на главную страницу.
        """
        # Вводим данные
        self.find_element(self.USERNAME_FIELD).send_keys(username)
        self.find_element(self.PASSWORD_FIELD).send_keys(password)
        self.find_clickable_element(self.LOGIN_BUTTON).click()

        # Ждем перехода на главную страницу
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("inventory")
        )