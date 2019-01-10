import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome('C:/Users/Hong/AppData/Local/Programs/Python/chromedriver.exe')
driver = webdriver.Chrome('/Users/lhj/chromedriver')  # mac or linux

driver.get("https://www.google.com")
time.sleep(2)

inputElement = driver.find_element_by_name("q")
inputElement.send_keys("세종대왕")
inputElement.submit()        # cf.  inputElement.send_keys(Keys.RETURN)

time.sleep(5)                # cf.  driver.implicitly_wait(5)
driver.quit()