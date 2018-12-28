# coding=utf-8
import cx_Oracle

connection = cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")
print(connection.version)

# cursor를 만들어줍니다
cursor = connection.cursor()

query = ''' select * from Departments '''

# 실행을 시킵니다.
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
