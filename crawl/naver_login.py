import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = '/Users/lhj/chromedriver'
driver = webdriver.Chrome(drvPath)

driver.get("https://www.naver.com")
time.sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()
time.sleep(1)

driver.execute_script("document.getElementById('id').value = '본인 아이디';")
driver.execute_script("document.getElementById('pw').value = '본인 비밀번호';")

pw = driver.find_element_by_id('pw')
pw.send_keys(Keys.RETURN)


time.sleep(5)        

