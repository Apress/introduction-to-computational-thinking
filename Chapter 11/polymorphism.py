import math


class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height


class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2


def sum_of_areas(shapes):
    result = 0
    for shape in shapes:
        result += shape.area()
    return result

shapes = [Rectangle(10, 20), Rectangle(4, 50), Circle(3)]
print(sum_of_areas(shapes))



class Duck(object):
	def say(self):
		print("Quack!")

class Dog(object):
	def say(self):
		print("Wuff!")

class Worm(object):
	def say(self):
		print("...")

animals = [
	Duck(),
	Dog(),
	Worm()
]
for animal in animals:
	animal.say()
