x = [1, 5, -1, 6, -4, -3, 10]
sum = 0

for i in x:
    if i < 0:
        continue
    else:
        sum += i

print(f"Sum of non-negative numbers in the list is {sum}")
