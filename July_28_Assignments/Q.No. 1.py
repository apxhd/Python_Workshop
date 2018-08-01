# Program that contains a class with get function and set function


class Student:
    name = ''

    @classmethod
    def setString(cls,name):
        cls.name = name

    @classmethod
    def getString(cls):
        return cls.name.upper()


Student.setString(input("Enter your name:"))
print(Student.getString())
