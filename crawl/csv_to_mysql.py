import pymysql
import csv
import codecs


def get_conn(db):
  return pymysql.connect( 
        host = 'localhost',
        user = 'doo',
        password = '11' ,
        port = 3306 ,
        db = db ,
        charset = 'utf8' )


csvFile = codecs.open('crawl/melon_top100.csv','r','utf-8')
reader = csv.reader(csvFile, delimiter=',', quotechar='"')

lst = []

for row in reader :
    lst.append([row[0],row[1],row[2],row[3]])

del lst[0]
del lst[ len(lst) - 1]

sql_truncate = "truncate table MelonTop"
sql_insert = "insert into MelonTop(rank, title, singer, likecnt) values(%s, %s, %s, %s)"

conn = get_conn('doodb')

with conn:
    cur = conn.cursor()
    cur.execute(sql_truncate)
    cur.executemany(sql_insert, lst)
    print('반영된 것', cur.rowcount)