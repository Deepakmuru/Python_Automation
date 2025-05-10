import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#Sum validation

prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount = float(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert  sum == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 8)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

