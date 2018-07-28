def squared(x):
    return x ** 2


print(squared(2))
print((lambda x,y: x ** y)(2,3))


#lambda
y = lambda a, b: a*b
print(y(2,3))

#2
gen = lambda x: list(range(x)) if not x < 0 else []
print(gen(4))
print(gen(-1))


#map
def square(x):
    return x**2


#print(square([1, 2, 3, 4]))
p =list(map(square, [1, 2, 3, 4]))
print(p)

#Concise
print(list(map(lambda x: x**2, [1,2,3,4])))

print(set(map(lambda x: x**2, [1,2,3,4,3,4,9])))


#Filter

def fil(x):
    l = []
    for each in x:
        if each > 3:
            l.append(each)
    return l


print(fil([1,2,3,4,5,6]))

#concise
print(list(filter(lambda x: x>3,[1,2,3,4,5,6])))


#reduce function
from functools import reduce

redu = reduce(lambda x, y: x+y, [1,3,6,3,4])
print(redu)


#enumerate

for x, y in enumerate([1,2,3,4,], start = 100):
    print(x, y)


#Dictionary comprehension

d = {}
for x, y in zip([1,2,3],["a","b","c","d"]):
    d[x] = y
    print(x, y)
print(d)

keys = [1,2,3,4]
values = ["a","b","c"]
di = {x:y for x,y in zip(keys,values)}
print(di)



#set comprehension

nums = [1,2,3,4,5,5]
my_set = { val*val for val in nums}
print(my_set)







