import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless") #the script will run without showing the browser opening
chrome_options.add_argument("--ignore--cetificate--errors") #it will ignore any certificate error on the website

service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") #execute javascript
driver.get_screenshot_as_file("screen.png")
