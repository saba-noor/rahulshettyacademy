from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch browser
driver = webdriver.Chrome()

# Step 2: Open website
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.maximize_window()


#add products
buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'btn-info')]")

for btn in buttons:
    btn.click()
    time.sleep(1)
#go to checkout page
driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]").click()
time.sleep(2)

driver.quit()