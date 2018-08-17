#Program to count number of each character in string


chars = "abcdefghijklmnopqrstuvwxyz"
new_str = input("Enter a string")

for char in new_str:
    count = new_str.count(char)
    if count > 1:
        print(char + ":" + str(count))