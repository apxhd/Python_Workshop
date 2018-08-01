class Rectangle:
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    @property
    def getData(self):
        return (self.length, self.breadth)


r1 = Rectangle(10, 20)
print(f"Area = {r1.area()}")
print(f"Length, Breadth = {r1.getData}")
