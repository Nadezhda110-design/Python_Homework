import pytest
from selenium import webdriver
from pages1.LoginPage import LoginPage
from pages1.MainPage import MainPage
from pages1.CartPage import CartPage
from pages1.CheckoutPage import CheckoutPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.mark.parametrize(
    "username, password, product_name, first_name, last_name, "
    "postal_code, expected_result, delay",
    [
        ("standard_user", "secret_sauce", "Sauce Labs Backpack",
         "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie","Иван",
         "Петров", "123456", "58.29"),

    ],
)

@allure.title("Тестирование оформления заказа")
@allure.description("Тест проверяет корректность оформления "
                    "заказа и проверяет итоговую сумму.")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_allure(driver):
    """
    Тест проверяет итоговую сумму при оформлении заказа

    :param driver:
    :param username:
    """

    with allure.step("Открытие страницы магазина"):
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
    with allure.step("Авторизация на странице"):
        login_page.authorize("standard_user", "secret_sauce")
    with allure.step("Добавление товаров в корзину"):
        main_page = MainPage(driver)
        products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
        ]
        for product in products:
            main_page.add_product_to_cart(product)
    with allure.step("Переход в корзину"):
        main_page.go_to_cart()
    with allure.step("Переход на страницу оформления заказа"):
        cart_page = CartPage(driver)
        cart_page.checkout()
    with allure.step("Заполнение формы заказа"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form("Иван", "Петров", "123456")
    with allure.step("Проверка итоговой суммы заказа"):
       actual_total = checkout_page.get_total_price()
       assert actual_total == "58.29", f"Ожидалось $58.29, получено ${actual_total}"
