import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path=
                        "C:\\Users\\Admin\\Selenium Jar\\Chrome Driver\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(5)
print(driver.title)

driver.get("https://www.flipkart.com")
time.sleep(5)
print(driver.title)

driver.back()
time.sleep(5)

driver.get("https://www.amazon.com")
print(driver.title)
time.sleep(5)
driver.back()
print(driver.title)
driver.close()
