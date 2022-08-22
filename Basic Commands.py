import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=
                          "C:\\Users\\Admin\\Selenium Jar\\Chrome Driver\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
time.sleep(8)
print(driver.title)
driver.close()
