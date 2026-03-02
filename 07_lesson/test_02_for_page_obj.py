from selenium import webdriver
from pages.CalculatorPage import CalculatorPage


def test_02_for_page_obj():
    driver = webdriver.Chrome()
    calculator_page = CalculatorPage(driver)
    calculator_page.open()
    calculator_page.set_delay(45)
    calculator_page.click_number("7")
    calculator_page.click_operator("+")
    calculator_page.click_number("8")
    calculator_page.click_equals()
    calculator_page.wait_for_result("15")
    actual_result = calculator_page.get_screen_text()

    assert actual_result == "15"

    driver.quit()



