import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


@pytest.fixture
def driver():
    """Фикстура для создания драйвера Firefox"""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_03_for_page_obj(driver):
    """Тест оформления заказа с проверкой итоговой суммы"""

    # 1. Авторизация
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login_page.authorize("standard_user", "secret_sauce")

    # 2. Добавление товаров
    main_page = MainPage(driver)
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product in products:
        main_page.add_product_to_cart(product)

    # 3. Переход в корзину и checkout
    main_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.checkout()

    # 4. Заполнение формы
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Иван", "Петров", "123456")

    # 5. Проверка итоговой суммы
    actual_total = checkout_page.get_total_price()
    assert actual_total == "58.29", f"Ожидалось $58.29, получено ${actual_total}"
