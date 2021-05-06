def bmi(patient):
    return patient.weight / (patient.height * 100)**2
    
class Patient(object):
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height * 100)**2

    def __repr__(self):
        return "Patient('{}', {}, {})".format(
            self.name, self.height, self.weight
        )

    def __str__(self):
        return "Patient {} is {} cm tall and weighs {} kg".format(
            self.name, self.height, self.weight
        )

george = Patient('George', 166, 89)
print(george)
print(bmi(george), george.bmi())

# From Python 3.7 an onwards, you get a different syntax for 
# defining classes, that will automatically generate some of the
# code for you
from dataclasses import dataclass

@dataclass
class Patient(object):
    name: str
    height: int
    weight: int

    def bmi(self):
        return self.weight / (self.height * 100)**2

george = Patient('George', 166, 89)
print(george)
print(bmi(george), george.bmi())