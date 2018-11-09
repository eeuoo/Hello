class Casting: 
    def to_int(s): 
        if type(s) == str: 
            return int(s.strip()) 
        else: 
            return s 

class 사각형: 
    name = "사각형" 
    msg = "가로와 세로는?(usage: 밑변, 높이)"

    def __init__(self): 
          print("------------------------") 
  
    def input_data(self): 
          datum = input(self.msg)  # 5, 3 
          data = datum.split(',')  # ['5', '3'] 
          x = Casting.to_int(data[0])
          if len(data) < 2:
              y = x
          else:
              y = Casting.to_int(data[1]) 

          self.__새넓이(x, y) 
  
 
    def __새넓이(self, x, y): 
          r = x * y 
          print("{}의 넓이는 {}입니다".format(self.name, r)) 
  
 
class 직사각형(사각형): 
    name = "직사각형" 
        
class 평행사변형(사각형): 
    name = "평행사변형" 
    msg = "밑변와 높이는?? (usage: 밑변, 높이)" 
  
class 정사각형(사각형): 
    name = "평행사변형" 
    msg = "한 변의 길이는??" 
    

all_rects = [사각형(), 직사각형(), 평행사변형(), 정사각형()] 

first_msg = "사각형의 종류는?\n"
for i, r in enumerate(all_rects):
    if i == 0:
        continue
    first_msg += "{:d}) {}\n".format(i, r.name)

first_msg += "(quit:q) >>"

while True: 

    print() 
    rect_type = input(first_msg)
    if (rect_type == 'q'): 
        break 


    rect_index = Casting.to_int(rect_type)
    if rect_index > len(all_rects):
        rect_index = 0 
    rect = all_rects[rect_index] 
    rect.input_data() 
