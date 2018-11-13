class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return "{}:{}".format(self.name, self.score)

students = [Student("김가수", 10), Student("김나수", 30), Student("김다수", 20)]

# print(students[0])

def print_students():
    print("-----------------")
    for s in students:
        print(s)

students = sorted(students,key = lambda stu : stu.score)
print_students()

students.sort(key = lambda stu : stu.name)
print_students()

