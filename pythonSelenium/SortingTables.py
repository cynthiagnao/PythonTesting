import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

browserSortedVeggies = []
time.sleep(2)

# cliquer sur l'entête de la colonne
driver.find_element(By.XPATH, "//span[normalize-space()='Veg/fruit name']").click()

# parcourir la colonne et mettre le contenu dans une liste -> browserSortedVeggieList
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy() #.copy() or .slice(), copy is faster than slice

# Trier cette liste browserSortedVeggieList -> newSortedList
browserSortedVeggies.sort()

# browserSortedVeggieList == newSortedList
assert originalBrowserSortedList == browserSortedVeggies
