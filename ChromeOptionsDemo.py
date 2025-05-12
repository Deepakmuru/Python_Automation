from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)