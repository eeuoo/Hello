
class Dog:
    def __init__(self, name):
        self.name = name
        self.color = "Blue"
        print(name, "was Born")

    def speak(self):
        print("YELP!", self.name)

    def wag(self):
        print("Dog's wag tail")
    
    def __del__(self):
        print("destroy!!")


class Puppy(Dog):
    def __init__(self, name):
        self.name = name
        print(name, "was Born")
    
    def __read_diary(self):
        print("diary txt")

    def wag(self):
        self.__read_diary()
        print("puppy's wag tail")

    def tto():
        print("eeee")


d = Dog('보리')
p = Puppy('쌀')
d.speak()
p.speak()

p.wag()

Puppy.tto()