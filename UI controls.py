import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
Radio = driver.find_elements(By.XPATH,"//input[@name='radioButton']")

print(len(Radio))

for checkbox in Radio:
    if checkbox.get_attribute("value") == "radio2":
        checkbox.click()
        assert checkbox.is_selected()
        break


time.sleep(2)


