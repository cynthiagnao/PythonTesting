import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(15)

# URL of the webpage you want to scrape
url = 'https://rahulshettyacademy.com/documents-request'
driver.get(url)



# Sample text content
text_content = driver.find_element(By.XPATH, "//div//p[2]").text

# Define a regular expression pattern for extracting the email address
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Use re.search to find the email address in the text content
match = re.search(email_pattern, text_content)

# Extract the email address if found
email = match.group(0) if match else None

# Print the email address
print(email)

time.sleep(2)
