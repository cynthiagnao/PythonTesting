import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)


#GO TO THE WEBSITE
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
time.sleep(2)

# click on the blinking link
driver.find_element(By.XPATH, "//a[@class='blinkingText']").click()

# child window opens
windowsOpened = driver.window_handles


#OPEN THE 2ND WINDOW

driver.switch_to.window(windowsOpened[1])
wholeText = driver.find_element(By.XPATH, "//div//p[2]").text

# Method 1
#email = wholeText[18:48]
#print(email)

# Method 2
# Define a regular expression pattern for extracting the email address
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# Use re.search to find the email address in the text content
match = re.search(email_pattern, wholeText)
# Extract the email address if found
email = match.group(0) if match else None
# Print the email address
#print(email)
time.sleep(2)


#GO BACK TO THE the 1ST WINDOW

# fulfill the form and submit
driver.switch_to.window(windowsOpened[0])
password = driver.find_element(By.XPATH, "//b/i[.='learning']").text
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "signInBtn").click()

# create an object for the Alert message css selector
display_none_element = driver.find_element(By.CSS_SELECTOR, 'div.alert.alert-danger.col-md-12[style*="display: none;"]')

# retrieve the Alert message text and print it
if display_none_element:
    text = display_none_element.get_attribute('textContent')
    print(text.strip())
else:
    print('Element with display: none not found.')

time.sleep(2)
