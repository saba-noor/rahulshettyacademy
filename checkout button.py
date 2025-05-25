from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch browser
driver = webdriver.Chrome()

# Step 2: Open website
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.maximize_window()
time.sleep(2)

# Step 3: Click on "Checkout" button
driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]").click()
time.sleep(2)

# Step 4: Close browser
driver.quit()
