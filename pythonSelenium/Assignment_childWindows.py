import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH, "//a[@class='blinkingText']").click()

windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
wholeText = driver.find_element(By.XPATH, "//div//p[2]").text
#var = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+',wholeText)
#print(var)
#print(wholeText[18:48])
email = wholeText[18:48]

driver.switch_to.window(windowsOpened[0])
password = driver.find_element(By.XPATH, "//b/i[.='learning']").text
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "signInBtn").click()

#print(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger col-md-12']"))).get_attribute("innerHTML"))
print(driver.execute_script("return document.getElementById('cdk-describedby-message-0').textContent;"))


#explicit wait target a specific element
'''wait = WebDriverWait(driver,10) #explicit wait target a specific element
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='alert alert-danger col-md-12']")))
alertMessage = driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']").text
print(alertMessage)
'''

#style="display: none;"
#errorMessage = driver.find_element(By.CLASS_NAME, "alert").text
#print(errorMessage)

#switch from browser mode to alert mode
'''alert = driver.switch_to.active_element
alertText = alert.text
print(alertText)
'''

time.sleep(2)
