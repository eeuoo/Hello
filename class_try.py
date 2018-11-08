class Quadrangle:
    def __init__(self, area):
        self.area = area

    def unit(self,area):
        self.area = self.area * area

        
class Rectangle(Quadrangle):   
    def __init__(self, area):
        self.area = area
        
    def unit(self,area):
        self.area = self.area * area

        
class Parallelogram(Quadrangle):
    def __init__(self, area):
        self.area = area
        
    def unit(self,area):
        self.area = self.area * area


box = Quadrangle(2)
box2 = Rectangle(3)
box3 = Parallelogram(1)

box.unit(22)
box2.unit(20)
box3.unit(24)

print (box.area, box2.area, box3.area)

cmd = input("사각형의 종류는? ->")

if cmd == 사각형:
    input("밑변과 높이 입력 ->")

elif cmd == 직사각형:
    input("가로와 세로 입력 ->")

elif cmd == 평행사변형:
    input("밑변과 높이 입력 ->")
