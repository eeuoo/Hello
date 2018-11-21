import sqlite3

conn = sqlite3.connect("student_try.db")

data = (
    (21, '김런던'),
    (22, '이서울')
)

with conn:
    cur = conn.cursor()
    sql = "insert into tt(id, name) values(?,?)"
    cur.executemany(sql, data)

    conn.commit()
