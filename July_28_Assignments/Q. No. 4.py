# Program with a circle class that has a area method and get radius property
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    @property
    def getRadius(self):
        return self.radius;


r1 = Circle(20)
print("Area =", end=' ')
print(r1.area())
print("Radius =", end=' ')
print(r1.getRadius)
