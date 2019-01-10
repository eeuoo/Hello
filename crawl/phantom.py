import time
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.implicitly_wait(3)

driver.get("https://www.naver.com")
time.sleep(2)

driver.save_screenshot("aaa.png")
driver.implicitly_wait(5)
driver.quit()