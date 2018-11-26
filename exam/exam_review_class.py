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
        print(g_level)
        if self.grade == 100: 
            return 'A+' 
        elif self.grade < 50:
            return 'F'    
        else: 
            return g_level[ self.grade  // 10 - 5 ] 


    def make_addr(self):
        self.sp_addr = self.addr.split(' ')
        ret = []
        gu = ''
        dong = ''
        
        for i in self.sp_addr:
            if i.find('구') == (len(i) - 1 ):
                gu = i
            elif i.find('동', 1) == (len(i) - 1 ):
                dong = i 
        
        return "{} {}".format(gu, dong)

    def make_gender(self):
        return 'F' if self.gender == '여' else 'M'
        
    def make_age(self):
        try:
            iage = (int(self.age) // 10) * 10
            return "{:d}0대".format(iage)            
        except:
            return '알 수 없음'


    def __str__(self):
        return "{}**, {}, {}, {}, {}".format(self.name[0], self.make_gender(), self.make_age(), self.level, self.make_addr())
 
    def make_params(self):
        return (self.name[0] + '**', self.make_gender(), self.make_age(), self.make_grade(), self.make_addr())
 