import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Cynthia")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()
#driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']").click()

sel = Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
sel.select_by_visible_text("Female")

driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

time.sleep(3)
