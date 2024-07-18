import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#-- Chrome
service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("12345")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("12345")
driver.find_element(By.XPATH, "//button[@type='submit']").click()


time.sleep(8)