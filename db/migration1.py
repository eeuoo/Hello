import pymysql

def get_mysql_conn(db):
    return pymysql.connect(
        host='localhost',
        user='doo',
        password='11',
        port=3306,
        db=db,
        charset='utf8')

conn_dooodb = get_mysql_conn('doodb')

# read from source db
with conn_dooodb:
    cur = conn_dooodb.cursor()
    sql = "select id, name, prof, classroom from Subject"

    cur.execute(sql)
    rows = cur.fetchall()

for row in rows:
    print(row)