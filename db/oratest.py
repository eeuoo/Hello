import cx_Oracle

connection = cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")
print(connection.version)

with connection:
   cursor = connection.cursor()

   sql = '''select * from Departments where department_id = :dept_id'''

   cursor.execute(sql, (30,))

   rows = cursor.fetchall()

for row in rows:
   print(row)
