# Program with Shape class and Square subclass

class Shape:
    def area(self):
        return 0;


class Square(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length ** 2


s1 = Square(20)
print(s1.area())
print(Square.__mro__)
