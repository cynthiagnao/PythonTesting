import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#-- Chrome
service_obj = Service("/Users/Lenovo/Desktop/QA Python/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# //a[contains(@href,'shop')]   a[href*='shop']
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()


products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Thank you" in successText #validate that the words 'Thank you' is present in the successText

time.sleep(2)

