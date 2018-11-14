from functools import reduce
from student_class import Student
        
students = []
with open ("students.csv","r", encoding = 'utf8') as file:
    for line in file:
        students.append( Student(line) )

students.sort(key = lambda stu : stu.score, reverse = True )
m = map(lambda stu: stu.make_grade(), students) 
list(m) 

total = reduce(lambda x, y : ( x if type(x) == int else x.score) + y.score, students)
avg = total / len(students)
print("총계, 평균 >", total, avg)

print("이름\t성별\t나이\t학점") 
print("----\t----\t----\t----") 

for s in students:
    print(s)

print("이름\t점수") 
print("------\t----")

for s in students:
    if s.score >= avg:
        print("{}\t{}".format(s.name, s.score))
