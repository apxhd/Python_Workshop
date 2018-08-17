#Program o print Hello World with the concept of file


with open("hello.txt", 'w') as fp:
    fp.write("Hello World")

with open("hello.txt", 'r') as fpr:
    print(fpr.read())


