import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.cricbuzz.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"a[title='Live Cricket Score']").click()
driver.find_element(By.ID,"international-tab").click()
time.sleep(2)