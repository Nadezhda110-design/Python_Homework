from selenium import webdriver
from lesson_10.pages2.CalculatorPage import CalculatorPage
import allure

@allure.title("Тестирование калькулятора: {num1} {operation} {num2} "
              "= {expected_result}")
@allure.description("Тест проверяет корректность работу калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)

def test_calc_allure():
    """
    Тест проверяет работу калькулятора.
    """
    with allure.step("Открытие браузера"):
        driver = webdriver.Chrome()
        calculator_page = CalculatorPage(driver)
    with allure.step("Открытие страницы калькулятора"):
        calculator_page.open()
    with allure.step("Установка задержки 45 секунд"):
        calculator_page.set_delay(45)
    with allure.step("Нажатие кнопки 7"):
        calculator_page.click_number("7")
    with allure.step("Нажатие кнопки +"):
        calculator_page.click_operator("+")
    with allure.step("Нажатие кнопки 8"):
        calculator_page.click_number("8")
    with allure.step("Нажатие кнопки ="):
        calculator_page.click_equals()
    with allure.step("Ожидание результата 15"):
        calculator_page.wait_for_result(expected_result = "15")
    with (allure.step("Проверка результата")):
        actual_result = calculator_page.get_screen_text()

    assert actual_result == "15"
    with allure.step("Закрытие браузера"):
        driver.quit()



