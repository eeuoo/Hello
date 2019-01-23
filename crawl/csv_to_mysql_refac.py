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

sql_truncate = "truncate table MelonTop"
sql_insert = "insert into MelonTop(rank, title, singer, likecnt) values(%s, %s, %s, %s)"

def mysql_save(lst):

  try:
    conn = get_conn('doodb')
    conn.autocommit = False
    cur = conn.cursor()

    if lst != None and len(lst) > 0 :
      cur.execute(sql_truncate)

    cur.executemany(sql_insert, lst)
    conn.commit()
    print('반영된 것', cur.rowcount,"/100")

  except Exception as err:
    conn.rollback()
    print("Error", err)

  finally :
    try:
      cur.close()
    except:
      print("Error on close cursor")
    
    try: 
      conn.close()
    except Exception as err2:
      print("Fail to connect!!", err2)


lst = []

for row in reader :
  lst.append([row[0],row[1],row[2],row[3]])

del lst[0]
del lst[ len(lst) - 1 ]

mysql_save(lst)