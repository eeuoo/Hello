import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080') # 웹툰처럼 화면 긴 것은 해상도의 높이를 길게 주면 됨
options.add_argument("disable-gpu")    # or.   options.add_argument("--disable-gpu")
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

#driver = webdriver.Chrome('/Users/lhj/chromedriver', chrome_options=options)
driver = webdriver.Chrome('/Users/lhj/chromedriver', options=options)

driver.implicitly_wait(3)

driver.get("https://www.naver.com")
time.sleep(2)

driver.save_screenshot("bbb.png")   # or.  driver.get_screenshot_as_file('bbb.png')
driver.implicitly_wait(5)
driver.quit()