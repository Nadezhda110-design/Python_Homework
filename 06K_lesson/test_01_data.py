from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(driver, 50)

    data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field, value in data.items():
        element = wait.until(EC.presence_of_element_located((By.NAME, field)))
        element.clear()
        element.send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_field = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

    assert "alert-danger" in zip_field.get_attribute("class")

    green_fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]

    for field in green_fields:
        element = driver.find_element(By.ID, field)
        assert "alert-success" in element.get_attribute("class")

    driver.quit()
