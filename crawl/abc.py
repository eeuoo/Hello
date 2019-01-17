import json
from bs4 import BeautifulSoup
import csv, codecs
from pprint import pprint


html = '''
<table>
    <tr>
        <th>회사</th>
        <th>A사</th>
        <th>B사</th>
        <th>C사</th>
        <th>D사</th>
    </tr>
    <tr>
        <th>주소</th>
        <td>서울</td>
        <td>강원도</td>
        <td>부산</td>
        <td>대전</td>
    </tr>
    <tr>
        <th>직원수</th>
        <td>30명</td>
        <td>55명</td>
        <td>200명</td>
        <td>40명</td>
        
    </tr>
    <tr>
        <th>전화번호</th>
        <td>02-2345-2323</td>
        <td>033-223-2323</td>
        <td>051-121-1212</td>
        <td>010-333-444</td>
    </tr>
    <tr>
        <th>대표메일</th>
        <td>a@a.com</td>
        <td>b@b.com</td>
        <td>c@c.com</td>
        <td>d@d.com</td>
    </tr>
</table>
'''


soup = BeautifulSoup(html,'html.parser')

ths = soup.select('tr > th')
trs = soup.select('tr')

comp_info = []

for td in trs :
    th = td.select('td')
    comp_info.append(th)



infos = []

for i in ths :
    head = i.text
    infos.append(head)
    


print(infos)
print(comp_info[1])



companies_dic = {}

for j in range(0,len(comp_info[1])):
    tempdic ={}

    for i in range(4,len(infos)):
        try : 
            key = infos[i]
            value = comp_info[i-3][j].text

            tempdic[key] = value

        except IndexError:
            continue
        
    
    companies_dic[infos[j+1]] = tempdic


pprint(companies_dic)

company = { 'company' : companies_dic }

pprint(company)




# 회사정보 반환하는 함수
def get_com_info (com, info):
    a = companies_dic[com][info]

    print (a)

get_com_info('A사','전화번호')


# input 값 받아서 회사정보 반환하기
aa = input('회사와 알고 싶은 정보를 입력하세요 ( ex : A사, 전호번호) >>>')
bb = aa.split(',')
com = bb[0]
info = bb[1]

a = companies_dic[com][info]

print(a)





# for index, info in enumerate(comp_info):
#     tempdic = {}
#     if index == 0 :
#         continue
#     else : 
#         for i, x in enumerate(infos):
#             if i < 4 :
#                 continue
#             else : 

#                 print(x)
#                 # tempdic[x] = (info[0].text)

#                 # print(tempdic)



# for index, info in enumerate(infos) :
#     tempdic={}
#     if index < 4 :
#         continue
#     else : 
#         for i, x in enumerate(comp_info):

#             if i == 0 :
#                 continue
#             else : 
#                 x = 0
                  

dic =   { 'compaines' : [
            { 'A' : { 'a' : 'A1',
                      'b' : 'A2',
                    }
            }, 
            { 'B' : { 'a' : 'B1',
                      'b' : 'B2'
                    } 
            }, 
            { 'C' : { 'a' : 'C1',
                      'b' : 'C2'
                    } 
            }
                        ]
        }

