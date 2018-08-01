# Program to create MyException using Exception base class

class MyException(Exception):
    def __init__(self,text):
        self.text = text

    @property
    def getData(self):
        return self.text


e1 = MyException("This is a error.")
print(e1.getData)
print(MyException.__mro__)