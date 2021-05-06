import math
class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * radius**2

circ = Circle(2)
print(circ.radius, circ.area)
circ.radius = 4
print(circ.radius, circ.area) # wrong area!
print()

class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return math.pi * self.radius**2

# Ok, but new syntax; annoying to update everywhere
circ = Circle(2)
print(circ.radius, circ.get_area())
circ.radius = 4
print(circ.radius, circ.get_area())
print()

# the same if we change set radius. Here we are also at the
# risk that someone sets circ.radius = 12 in the code, and we
# won't get an error if that happens
class Circle(object):
    def set_radius(self, radius):
        self.radius = radius
        self.area = math.pi * radius**2
    def __init__(self, radius):
        self.set_radius(radius)

circ = Circle(2)
print(circ.radius, circ.area)
circ.set_radius(4)
print(circ.radius, circ.area) # ok
circ.radius = 2 # ups!
print(circ.radius, circ.area) # wrong area (we didn't update it)
print()


# Computed area when we access the attribute
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def __setattr__(self, name, value):
        if name == 'area':
            print("no way!")
        else: 
            super().__setattr__(name, value)

    def __getattr__(self, name):
        if name == 'area':
            return math.pi * self.radius**2
        else:
            return super().__getattribute__(name)

# Now things are working
circ = Circle(2)
print(circ.radius, circ.area)
circ.radius = 4
print(circ.radius, circ.area)
print()

# We are not allowed to change area (an exception would probably be better)
circ.area = 4


class Circle(object):
    def __setattr__(self, name, value):
        if name == 'radius':
            self.__dict__['radius'] = value
            self.__dict__['area'] = math.pi * value**2
        elif name == 'area':
            print("no way!")
        else:
            super().__setattr__(name, value)

    def __init__(self, radius):
        self.radius = radius

circ = Circle(2)
print(circ.radius, circ.area)
circ.radius = 4 # this sets both radius and area
print(circ.radius, circ.area)
print()


# Using properties
class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return math.pi * self.radius**2

    # this is the magic
    area = property(get_area)

circ = Circle(2)
print(circ.radius, circ.area)
circ.radius = 4
print(circ.radius, circ.area)
print()


class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self._radius
    def set_radius(self, value):
        self._radius = value
        self.area = math.pi * self._radius**2

    # this is the magic
    radius = property(get_radius, set_radius)
    
circ = Circle(2)
print(circ.radius, circ.area)
circ.radius = 4
print(circ.radius, circ.area)
print()



# Using a decorator
class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return math.pi * self.radius**2

circ = Circle(2)
print(circ.radius, circ.area)
circ.radius = 4
print(circ.radius, circ.area)
print()


# Using a decorator + dataclass (Python 3.7 and up)
from dataclasses import dataclass
@dataclass
class Circle(object):
    radius: float
    @property
    def area(self) -> float:
        return math.pi * self.radius**2

circ = Circle(2)
print(circ.radius, circ.area)
circ.radius = 4
print(circ.radius, circ.area)
print()