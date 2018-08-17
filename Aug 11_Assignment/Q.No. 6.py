#Program to find square of list and display the even numbers using map and filter

print(list(map(lambda y: y**2, (filter(lambda x: x%2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))))

