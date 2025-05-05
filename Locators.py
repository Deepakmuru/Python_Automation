
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()

# ID, Xpath, CSSSelector, Classname, name, linktext

driver.find_element(By.ID,"login2").click()
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID,"loginusername"))
)

driver.find_element(By.ID,"loginusername").send_keys("Testscript")
driver.find_element(By.ID,"loginpassword").send_keys("Testscript")
driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary")
