class Navi:
    def __init__(self, title, url):
        self.title  =   title 
        self.url = url
        print((title, url))
        

f = Navi("s","sa")


class MyTuple(tuple):
    def __new__(self, x, y):
        return tuple.__new__(self, (x, y))

x = MyTuple("a","b")

print(x)