import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.find_element(By.ID,"cartur").click()
driver.find_element(By.CSS_SELECTOR,"button.btn.btn-success").click()
time.sleep(3)
driver.find_element(By.ID,"name").send_keys("Deepak Testing")
driver.find_element(By.ID,"country").send_keys("India")
driver.find_element(By.ID,"city").send_keys("Bangalore")
driver.find_element(By.ID,"card").send_keys("564555645435")
driver.find_element(By.ID,"month").send_keys("May")
driver.find_element(By.ID,"year").send_keys("2025")
driver.find_element(By.XPATH,"//button[@onclick='purchaseOrder()']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='confirm btn btn-lg btn-primary']").click()
time.sleep(3)