from bs4 import BeautifulSoup


melon_data = ''' <dl class="info_02 clfix">
                <dt>국적</dt>
                <dd>대한민국</dd>

                <dt>활동유형</dt>
                <dd>여성, 솔로</dd>

                <dt>활동년대</dt>
                <dd>2010</dd>
                
                <dt>활동장르</dt>
                <dd>Dance, Ballad, Drama</dd>
            
                <dt>데뷔</dt>
                <dd class="debut_song">
                    <span class="ellipsis">
                        2016.05.05
                        <span class="bar">
                            TTT
                        </span>
                    </span>
                </dd>
                
                <dt>생일</dt>
                <dd>1996.02.09</dd>
            </dl>'''


soup = BeautifulSoup(melon_data, 'html.parser')

cols = soup.select('dt')
rows = soup.select('dd')

keys = []
values = []
melon_dic = {}


for a in cols:
    keys.append(a.text)

for i in rows:
    a = i.find('span')
    if a != None :
        j = a.next.strip()
    else :
        j = i.text
    
    values.append(j)


for i in range(len(keys)):
    melon_dic[keys[i]] = values[i]

print(melon_dic)


col_names = {'국적': 'nation', '활동유형': 'act_type', '활동연대': 'act_year', '활동장르': 'act_genre', '데뷔': 'debut', '생일': 'birth'}