import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected() #return yes if it is checked
        break

time.sleep(2)

#Radio Buttons using XPATH
radiobuttons = driver.find_elements(By.XPATH, "//input[@name='radioButton']")
print(len(radiobuttons))

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()
        break

time.sleep(2)

#Radio Buttons using CSS_Selector
radiobuttonsA = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
print(len(radiobuttonsA))
radiobuttonsA[0].click()
assert radiobuttonsA[0].is_selected()

#Is the Box displayed ?
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

time.sleep(2)
