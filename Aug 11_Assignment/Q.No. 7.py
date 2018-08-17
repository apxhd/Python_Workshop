#Program for division with zero division error handling

num1 = int(input("Enter the 1st number:"))
num2 = int(input("Enter 2nd number:"))

try:
    div = lambda n1, n2: n1/n2
    print(div(num1, num2))

except ZeroDivisionError:
    print("Zero division not allowed")
