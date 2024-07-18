import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#-- Chrome
service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Locators : ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath - //tagname[@attribute='value'] -> //input[@type='submit']
# CSS - tagname[attribute='value'] -> //input[@type='submit'] , #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Cynthia")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click() #another way #driver.find_element(By.XPATH, "//label[@for='inlineRadio2']").click()

#Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")
#dropdown.select_by_value()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

time.sleep(8)
