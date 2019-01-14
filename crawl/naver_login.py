import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = '/Users/lhj/chromedriver'
driver = webdriver.Chrome(drvPath)
UserId1 = "dlgus"
UserId2 = "wn512"

UserPw1 = ""
UserPw2 = ""

driver.get("https://www.naver.com")
time.sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()
print("click big button!!")
time.sleep(1)

id = driver.find_element_by_id('id')

id.click()

for i in UserId1:
    id.send_keys(i)

for i in UserId2:
    id.send_keys(i)

pw = driver.find_element_by_id('pw')

for i in UserPw1:
    pw.send_keys(i)

driver.find_element_by_id('pw').click()

for i in UserPw2:
   pw.send_keys(i)


pw.send_keys(Keys.RETURN)


time.sleep(5)        

