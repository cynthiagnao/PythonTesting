import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://the-internet.herokuapp.com/iframe")
#close alert message
driver.find_element(By.XPATH, "//button[@class='tox-notification__dismiss tox-button tox-button--naked tox-button--icon']").click()

driver.switch_to.frame("mce_0_ifr") #you can use ID or Name
time.sleep(3)
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)

time.sleep(3)

