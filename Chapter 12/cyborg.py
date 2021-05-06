class Person(object):
    def __init__(self, name):
        print("Creating", name)
        self.name = name
    def hi(self):
        print("Hi from", self.name)
    def my_name(self):
        return self.name

class Robot(object):
    def __init__(self, name):
        print("rebooting...")
        super().__init__(name)
    def hi(self):
        print("0110001010")

class Cyborg(Robot, Person):
    def __init__(self, name):
        super().__init__(name)

robocop = Cyborg("Alex Murphy")
robocop.hi()
