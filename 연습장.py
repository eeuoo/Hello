def to_int(s):
    if type(s) == str:
        return int(s)

    else:
        return s

class 사각형:
    def __init__(self):
        print("사각형의 넓이")
    
    def 넓이(self, x, y):
        return to_int(x) * to_int(y)

class 직사각형(사각형):
    def __init__(self):
        print("직사각형의 넓이")

class 평행사변형(사각형):
    def __init__(self):
        print("평행사변형의 넓이")


while True:
    print()
    rect_type = input('사각형의 종류 1.직사각형 , 2.평행사변형 , 끝내고 싶으면 q >>')

    if (rect_type == 'q'):
        break

    입력값 = input("가로와 세로는?")
    가로, 세로 = 입력값.split(',')    

    if rect_type == '1':
        rect1 = 직사각형()
        결과 = rect1.넓이(가로, 세로)
    
    else :
        rect2 = 평행사변형()
        결과 = rect2.넓이(밑변, 높이)
        
    print(결과)

