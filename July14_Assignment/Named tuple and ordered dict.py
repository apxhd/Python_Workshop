from collections import namedtuple, OrderedDict

student = namedtuple('Student', ['Roll', 'Name', 'Batch'])

roll = input("Enter Roll No.")
name = input("Enter Name:")
batch = input("Enter Batch:")

st1 = student(roll, name, batch)
print(st1)

Student = {
    "Roll": 1,
    "Name": 2,
    "Batch": 3
}

Student_dwit = OrderedDict(Roll=roll, Name=name, Batch=batch)

print(Student_dwit)
print(dict(Student_dwit))


