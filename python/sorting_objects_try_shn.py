from functools import reduce
g_grades = ['A', 'B', 'C', 'D', 'F'] 
g_grades.reverse() 
  
class Student:
    grade = '' 
    def __init__(self, line): 
        name, gender, age, score = line.strip().split(',') 
        self.name = name 
        self.gender = gender           
        self.age = age 
        self.score = int(score) 
  
 
    def __str__(self): 
         return "{}**\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.grade) 
  
 
    def make_grade(self): 
          if self.score == 100: 
              self.grade = 'A+' 
          else: 
              self.grade = g_grades[ self.score // 10 - 5 ] 
 
 
students = [] 
with open('students.csv', 'r') as file: 
    for i, line in enumerate(file): 
        if i == 0: continue 
            students.append( Student(line) ) 

 
students.sort(key = lambda stu: stu.score, reverse = True) 
m = map(lambda stu: stu.make_grade(), students) 
list(m) 

total = reduce(lambda x, y : ( x if type(x) == int else x.score) + y.score, students)
print(total, total / len(students))

print("이름\t성별\t나이\t학점") 
print("----\t----\t----\t----") 

for s in students: 
     print(s) 
