from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")
sleep(2)
blue_button = driver.find_element(By.XPATH, "//button[contains(., 'Button')]")
blue_button.click()
sleep(2)

driver.quit()