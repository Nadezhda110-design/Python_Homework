from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
sleep(2)
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(1)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
sleep(2)

flash = driver.find_element(By.ID, "flash")
message = flash.text.replace("×", "").strip()
print(f"Сообщение после входа: {message}")

sleep(1)

driver.quit()