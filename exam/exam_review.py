#  students.csv 열기
# 데이터 변환
# 저장
# select


import sqlite3
from exam_review_class import Student  



params = []

with open ("students.csv", "r", encoding = 'utf8') as file:
    for i, line in enumerate(file):
        if i == 0 : continue
        stu = Student(line)
        t = stu.make_params()
        params.append(t)

print(params)

conn = sqlite3.connect("exam.db")

def insert_data():
    with conn:
        cur = conn.cursor()
        sql = "insert into Student(name, gender, age, grade, addr ) values(?,?,?,?,?)"        
        cur.executemany(sql, params)
        
        conn.commit()

def select_data():
     with conn:
        cur = conn.cursor()
        # sql = "select id, name, gender, age, grade, addr from Student values(?,?,?,?,?)"  
        sql = """select id, name, gender, age, grade, addr from Student order by substr(grade,1,1), grade desc """ 

        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)

        # print 할 거니까 Commit은 안 해도 됨    