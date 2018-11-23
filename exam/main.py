g_level = ['A', 'B', 'C', 'D', 'F'] 
g_level.reverse() 


class Student:
    level = ''
    def __init__(self, line):
        name, gender, age, grade, addr = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.grade = int(grade)
        self.addr = addr
    
    def make_grade(self):
        if self.grade == 100: 
            self.level = "A" 
        else: 
            self.level = g_level[ self.grade  // 10 - 5 ] 

    def make_addr(self):
        self.sp_addr = self.addr.split(' ')
        self.mk_addr = "{} {}".format(self.sp_addr[1],self.sp_addr[2])
        return self.mk_addr

    def make_gender(self):
        if self.gender == '여':
            return 'F'
        else: 
            return 'M'

    def make_age(self):
        return (int(self.age) // 10) * 10            

    def __str__(self):
        return "('{}**', '{}', {}, '{}', '{}')".format(self.name[0], self.make_gender(), self.make_age(), self.level, self.make_addr())



students = []
with open ("students.csv","r", encoding = 'utf8') as file:

    for i, line in enumerate(file):
        
        if i == 0 : continue
        students.append( Student(line) )


m = map(lambda stu: stu.make_grade(), students) 
list(m) 


data = []

for i in students:
    print(i)
    data.append(i)

print("\ndata >>>", data)

# import sqlite3
 
# conn = sqlite3.connect("exam.db")

# with conn:
#     cur = conn.cursor()
#     sql = "insert into Student(name, gender, age, grade, addr ) values(?,?,?,?,?)"        
#     cur.executemany(sql, data)
    
#     conn.commit()
