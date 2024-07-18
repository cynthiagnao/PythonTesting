import time

from selenium import webdriver
#from selenium.webdriver.chrome.service import Service

#Chrome driver service Selenium 160 -> chrome driver

#method by downloading browser driver 
#service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://www.genesispearl.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)


time.sleep(5)
