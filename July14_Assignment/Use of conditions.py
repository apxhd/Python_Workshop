age = int(input("Enter you age: "))
if age <= 1:
    print("Infant")
elif 1 < age <= 10:
    print("Child")
elif 10 < age <= 18:
    print("Teen")
elif 18 < age <= 45:
    print("Adult")
else:
    print("Old")
