x = list(range(1,20))

sum = 0
for i in x:
    sum += i
    if sum > 34:
        break

print(f"Sum is {sum}\n")
