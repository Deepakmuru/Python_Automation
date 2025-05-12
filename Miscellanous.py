import time

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,700);")
driver.get_screenshot_as_file("screen.png")
time.sleep(2)
