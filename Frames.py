import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"div.tox-icon").click()
driver.switch_to.frame("mce_0_ifr")
driver.execute_script("arguments[0].innerHTML = '';", driver.find_element(By.ID, "tinymce"))
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)