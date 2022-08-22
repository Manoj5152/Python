from selenium import webdriver

driver = webdriver.Chrome(executable_path=
                          "C:\\Users\\Admin\\Selenium Jar\\Chrome Driver\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.google.com")
print(driver.title)

driver.close()