#Program to read a file using try except and finally


try:
    fp = open('hello.txt','r')
    print(fp.read())
    fp.write("Hello Again")

except:
    print("Sorry we encountered a problem. Please check the syntax.")

finally:
    fp.close()