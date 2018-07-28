class Student:
    """
    This is the Student class
    """
    def __init__(self, first_name, last_name, roll_number, _class):
        self.first_name = first_name
        self.last_name = last_name
        self.roll_number = roll_number
        self._class = _class
        self.email = (self.first_name+'.'+self.last_name+'@deerwalk.edu.np').lower()

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.get_full_name()


x = ["Aabiskar","Pandey",701,"2nd Sem"]
s = Student(*x)
print(s)
print(s.get_full_name()) #OR
print(Student.get_full_name(s))
print(s.__doc__)
print(s.email)
print(dir(s))
print(s.__dict__)  #gives the data set in the attributes of the object
print(isinstance(s, Student))
print(isinstance(s, object))


#* = variable length argument

#Class variable

class Students:
    college = "DWIT"

    def __init__(self,name):
        self.name = name

    def get_college_name(self):
        return self.college

s = Students("Aabiskar Pandey")
print(dir(s))
s2 = Students("Sagar Giri")
print(dir(s2))
print(s.college)
print(s2.college)
print(s.get_college_name())


#class methods
class Studentss:
    count = 0
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        Studentss.count += 1

    @classmethod #decorator
    def create_student_from_string(cls, full_name):  #class method
        first, last = full_name.split(' ')
        return cls(first,last)

name1 = "Aabiskar Pandey"
name2 = "Sagar Giri"
s1 = Studentss.create_student_from_string(name1)
print(s1.count)
s2 = Studentss.create_student_from_string(name2)
print(s2.count)

print(s1.__dict__)
print(s2.__dict__)
