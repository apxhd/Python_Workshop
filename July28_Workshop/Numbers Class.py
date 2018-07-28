class Numbers():
    MULTIPLIER = 10

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls,a):
        return a * cls.MULTIPLIER

    @staticmethod
    def substract(a, b):
        return a - b

    @property
    def value(self):
        tup = (self.x, self.y)
        return tup

    @value.setter
    def value(self,tupzz):
        self.x = tupzz[0]
        self.y = tupzz[1]
        tup = (self.x ,self.y)
        return tup

    @value.deleter
    def value(self):
        del self.x
        del self.y

n1 = Numbers(2,5)
print(n1.add())
print(Numbers.multiply(5))
print(Numbers.substract(10,5))
print(n1.value)
n1.value = (100,50)
print(n1.value)
del n1.value
print(n1.__dict__)

