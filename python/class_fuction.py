class TestClass:
    name = "Test"

    def __init__(self):
        print("tttttttt")

    def get_name(self):
        print("00000000000")
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
        print (self.full_name)

    @property
    def full_name(self):
        return self.name + "rrrrr"

    def area(self, x, y):
        return x * y    

    @staticmethod
    def static_method():
        print("STATIC!!")    

class Child(TestClass):
    name = "child"
    def __init__(self):
        super().__init__()
        print("qqqqqqqqqqq")

    def get_name(self):
        super().get_name()
        return "Child name" + self.name

    def area(self, x, y):
        t = super().area(x, y)
        return t / 2

test = TestClass()
child = Child()

print(test.full_name)

print(test.area(2,3))
print(child.area(2,3))

getattr(test,'get_name')()
getattr(TestClass,"static_method")()

# cmd = input("input fuction >> ")
# getattr(test, cmd)()

test.static_method()
TestClass.static_method()
