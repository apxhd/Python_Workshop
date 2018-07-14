python = {
    "students": ["a","b","c"],
    (1,):"abc",
    1:"dsds"
}

print(python)
print(python['students'])  #try to avoid this way
print(python.get("students","Not Found")) # if key mistake, it returns none not error
print(python.get("studentss","Not Found")) # if key mistake, it returns none not error


python_class = {
    "students":{
        "a" : [10,20,30],
        "b": [100,200,300],
        "c":[10,20,30,(100,)]
    },
    "teacher" : "XYZ",
    "colleges" : ["DWIT","ASCOL"],
    "random" : ("P","M"),
    "random2" : set([1,2,3,3])
}

print(type(python_class))
print(python_class)
print(python_class.pop("random2"))


#loop in dict
for key, val in python_class.items():
    print(key,val)
print("="*20)

#for only values
for val in python_class.values():
    print(val)

#for key
for key in python_class.keys():
    print(key)

for key in python_class.keys():
    print(python_class.get(key))



#multiple dict and update

x = {
     "a" : 1,
     "b" : 2
}
y = {
     "a" : 100,
     "x": 5
}

x.update(y) #updates the value from y to x
print(x)


#OR

x = dict(name = "abc", age = 20, time= "now")
print(x)



x = ['c','b','a']
x.sort()
print(x)
x.sort(reverse = True)
print(x)
x.sort()
x.reverse()
print(x)
print(sorted(x,reverse = True))
