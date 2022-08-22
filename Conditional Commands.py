from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=
                          "C:\\Users\\Admin\\Selenium Jar\\Chrome Driver\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.saucedemo.com")

Lion = driver.find_element(By.ID, "user-name")

print(Lion.is_displayed())

Tiger = driver.find_element(By.XPATH, "//input[@id='password']")

print(Tiger.is_enabled())

driver.close()

