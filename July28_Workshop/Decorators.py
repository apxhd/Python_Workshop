#classmethod

class Person:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    @classmethod
    def obj_from_dict(cls, di):
        l_obj = []
        for each in di:
            name = each.get("name")
            address = each.get("address")
            l_obj.append(cls(name, address))

        return l_obj


d = [
    {"name": "Test", "address": "Chahbahil"},
    {"name": "Test2", "address": "Baneswor"}
]
p = Person.obj_from_dict(d)
print(p)


#staticmethod

from math import pi
class Geometry:

    @staticmethod
    def area_of_circle(r):
        return pi * (r**2)

    @staticmethod
    def circumference_of_circle(r):
        return 2 * pi * r

    @staticmethod
    def area_of_rectangle(l,b):
        return l * b

print(Geometry.area_of_circle(5))
print(Geometry.area_of_rectangle(5,4))


#workday checker

import datetime
class DateTimeWrapper():

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

my_date = datetime.date(2018, 7, 28)
is_workday = DateTimeWrapper.is_workday(my_date)
print("Is {} workday ? -> {}".format(my_date,is_workday))



#@property

class Employee:

    def __init__(self,fname,lname):
        self.first = fname
        self.last = lname

    @property
    def email(self):
        return self.first + "." + self.last + "@company.com"

    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    @fullname.setter # this is setter
    def fullname(self,name):
        first,last = name.split(" ")
        self.first = first
        self.last = last

        @fullname.deleter  # this is setter
        def fullname(self):
            del self.first
            del self.last


emp1 = Employee("Sagar","Giri")
print(emp1.fullname)
print(emp1.email.lower())

print("-------After Setter----------")
emp1.fullname = "Aabiskar Pandey"
print(emp1.fullname)
print(emp1.email.lower())

print("-------After Deleter--------")
del emp1.fullname
print(emp1,__dict__)
