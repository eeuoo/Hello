import random
import sqlite3

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")


def make_name():
    sung = random.choice(fam_names)
    name = "".join(random.sample(first_names, 2))
    return (sung + name,)

# QQQ
# print(make_name())
# exit()

data = []

for i in range(0,100):
    data.append(make_name())

# print(data)
# exit()

conn = sqlite3.connect("test.db")

 
with conn:
    cur = conn.cursor()
    sql = "insert into Student(name) values(?)"
    cur.executemany(sql, data)
    
    conn.commit()
   
print("99999")