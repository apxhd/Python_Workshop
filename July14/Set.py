x = set([1,2,3,3])
y = set([3,4,5])
p = set([5])

print(x.intersection(y))
print(x.difference(y))
print(x.union(y))
print(p.issubset(y))
print(y.issuperset(y))