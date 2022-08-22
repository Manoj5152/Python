from selenium import webdriver
from selenium.webdriver.common.keys import Keys

d = webdriver.Chrome(executable_path=
                          "C:\\Users\\Admin\\Selenium Jar\\Chrome Driver\\chromedriver_win32\\chromedriver.exe")
d.get("https://www.saucedemo.com/")
print(d.title)
print("-------------------")
print(d.current_url)
print("-------------------")
print(d.page_source)
print("-------------------")
d.close()