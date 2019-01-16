from time import sleep
from selenium import webdriver
import requests


USER = "dlguswn512"
PASS = ""

browser = webdriver.Chrome('/Users/lhj/chromedriver')
browser.implicitly_wait(3)

# 로그인 페이지에 접근하기. 
url_login = "https://www.yes24.com/Templates/FTLogin.aspx?ReturnURL=http://ticket.yes24.com/Pages/Perf/Detail/DetailSpecial.aspx&&ReturnParams=IdPerf=32059"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

# 아이디와 비밀번호 입력하기.
e = browser.find_element_by_id("SMemberID")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("SMemberPassword")
e.clear()
e.send_keys(PASS)

# 입력 양식 전송해서 로그인하기.
form = browser.find_element_by_css_selector("button#btnLogin").submit()
print("로그인 버튼을 클릭합니다.")

# 예매버튼 클릭.
reserve_bt = browser.find_element_by_class_name("rbt_reserve").click()
print("예매 버튼을 클릭합니다.")

# 팝업 창으로 전환.
browser.switch_to.window(browser.window_handles[1])

# 날짜 선택하기(26일)
date_sel = browser.find_element_by_css_selector("td.select > a").click()


sleep(1)

# 좌석 선택 버튼 클릭.
browser.find_element_by_css_selector("div.fr img").click()

# browser.execute_script('./jquery.js');
# browser.execute



seats = browser.find_elements_by_css_selector("ul.hi > li")

for seat in seats :

    print(seat.text)






# for i in seat:
#     a = i.text
#     print(i)


# print(seat)
# for s in seat:
#     print("-", s.text)


# 브라우저 닫음
# browser.close()



