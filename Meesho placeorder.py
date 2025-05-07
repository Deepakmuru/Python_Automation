import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.meesho.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[contains(text(),'Shop Now')]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//img[@alt='Useful Clothes Covers']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Add to Cart']").click()
time.sleep(5)