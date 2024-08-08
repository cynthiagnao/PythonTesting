from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)
driver.maximize_window()
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.PARTIAL_LINK_TEXT, "Free Access")).click().perform()

windows=driver.window_handles
driver.switch_to.window(windows[1])
grabbedtext = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
email = ""
grabbedtext = grabbedtext.split(" ")
for i in grabbedtext:
    if '@' in i:
        email = i
        break

driver.close()
driver.switch_to.window(windows[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("leaning")
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait_obj = WebDriverWait(driver, 10)
wait_obj.until(
    expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger col-md-12']")))

print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)