from collections import namedtuple

point= namedtuple('Point',['x','y'])
p = point(2,3)
print(p)

color = namedtuple('Color',['red','green','blue'])
c = color(255,255,255)
print(c)


#ordered dictionary
from collections import OrderedDict
x= {
    "a" : 1,
    "b" : 2,
    "c" :3
}
y = OrderedDict(a=1,b=2)

print(y)
print(dict(y))