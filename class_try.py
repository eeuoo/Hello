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


cmd = input("사각형의 종류는? ->")

if cmd == "사각형":
    higosa = input("밑변과 높이 입력 ->")
    hirosas = hirosa.split(',')
    
    a = int(hirosas[0])
    b = int(hirosas[1])

    box1 = Quadrangle(a)
    box1.unit(b)

    print (box1.area)

elif cmd == "직사각형":
    hirosa = input("가로와 세로 입력 ->")
    hirosas = hirosa.split(',')
    
    a = int(hirosas[0])
    b = int(hirosas[1])

    box2 = Rectangle(a)
    box2.unit(b)

    print (box2.area)

elif cmd == "평행사변형":
    hirosa = input("밑변과 높이 입력 ->")
    hirosas = hirosa.split(',')
    
    a = int(hirosas[0])
    b = int(hirosas[1])

    box3 = Parallelogram(a)
    box3.unit(b)
    
    print (box3.area)

