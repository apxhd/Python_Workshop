x = list(range(1,11))

print(x[3:6])
print(x[::-1])
print(x[3:-8])

x = [1,2,3,4,5]

y=[]
for each in x:
    y.append(each** 2)
print(y)

#or

y=[each**2 for each in x]
print(y)


#or comprehension

y = [each**2 for each in x if each!=4]
print(y)