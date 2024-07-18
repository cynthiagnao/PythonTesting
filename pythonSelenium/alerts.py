import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "Cynthia"
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "confirmbtn").click()

#switch from browser mode to alert mode
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept() #OK
#alert.dismiss() #cancel

time.sleep(2)
