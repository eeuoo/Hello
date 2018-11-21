import sqlite3
 
conn = sqlite3.connect("student_try.db")
 
with conn:
    cur = conn.cursor()
    sql = "select * from Student where id=? or name=?"

    rows = cur.execute(sql, (4, '홍길순'))
    
    # cur.execute(sql)
    # row = cur.fetchall()
 
for x in rows:
    print(x)
