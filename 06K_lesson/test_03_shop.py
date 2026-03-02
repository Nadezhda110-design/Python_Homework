from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_total():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    item_ids = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie",
    ]
    for item_id in item_ids:
        wait.until(
            EC.element_to_be_clickable((By.ID, item_id))
        ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Nadezhda")
    driver.find_element(By.ID, "last-name").send_keys("Babkina")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    total_label = wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, ".summary_total_label"))
        ).text

    assert total_label == "Total: $58.29"

    driver.quit()
