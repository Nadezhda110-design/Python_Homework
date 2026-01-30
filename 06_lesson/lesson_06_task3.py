from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_images_to_load(driver, timeout=10):

    wait = WebDriverWait(driver, timeout)

    wait.until(EC.presence_of_element_located((By.ID, "image-container")))

    def all_images_loaded(driver):
        images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
        if len(images) < 4:
            return False

        for img in images:
            if not img.get_attribute("complete"):
                return False
        return True

    wait.until(all_images_loaded)
    return driver.find_elements(By.CSS_SELECTOR, "#image-container img")

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

images = wait_for_images_to_load(driver)

if len(images) >= 3:
       third_image_src = images[2].get_attribute("src")
print(third_image_src)

driver.quit()

