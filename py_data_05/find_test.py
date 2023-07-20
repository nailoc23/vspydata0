import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
URL = 'https://www.nate.com/'
driver.get(URL)

ele_login_btn = driver.find_element(By.ID, 'btnLOGIN')
# print(ele_login_btn.tag_name)

ele_top_menu = driver.find_element(By.CLASS_NAME, 'chat1')
print(ele_top_menu.text)



time.sleep(10)
