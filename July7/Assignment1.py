#Assignment 1
#Aabiskar Pandey

# Script to find the acceleration from given data
print("Q.No. 1 \n")
v = 25
u = 0
t = 10
print("Given,\n v = {} m/s \n u = {} m/s \n t = {} sec".format(v,u,t))
print("a = (v-u)/t")
print("Accelaration = " + str((v-u)/t))


# Script to concatenate first and last names
print("\n Q.No. 2 \n")
fname = input("Enter first name :")
lname = input("Enter last name :")
print("Name : " + fname + " " + lname)


# Script to print arbitrary string 10 times
print("\nQ.No. 3 \n")
arb_string = input("Enter an arbitrary string :")
print((arb_string + " ") * 10)


# Script to override the end argument in print to **
print("\nQ.No. 4 \n")
print("This is a random string",end = "**")


# Script to demonstrate function of any 10 builtin functions
print("\nQ.No. 5 \n")
print("10 builtin functions in Python are : \n")

# pow()
print("1. Pow : Returns the power of a given number")
print(f"5 ^ 2 = {pow(5,2)}")

# ascii()
print("\n2. Ascii : Returns the character for any given value")
print(f"# = {ascii(65)}")

#str()
print("\n3. str : Converts and returns any data type into string")
print("Sum of 2 + 2 is" + str(4))

#int()
print("\n 4. int : Converts and returns any data data type into integer")
print(f"Int of 5.0 is {int(5.0)}")

#float()
print("\n 5. float : Converts and returns any data data type into floating point number")
print(f"Int of 11 is {float(11)}")

#ord
print("\n6. ord : Returns ascii value corresponding to any character")
print("Character represented by 65 is Ascii is {}".format(ord('A')))

#len
print("\n7. len : Returns the length of string or list or any sequence")
print("The length of 'MONTY PYTHON is {}".format(len("MONTY PYTHON")))

#complex()
print("\n8. complex : Returns the given numbers in complez form i.e in terms of j")
print(f"Complex form os 2 and 3 is {complex(2,3)}")

#abs()
print("\n9. abs : Returns the absolute value of given number")
print(f"Absolute value of -10 is {abs(10)}")

#divmod()
print("\n10. divmod() : Returns the quotient and remainder for any given numbers")
print(f"Quotient and remainder for 10/3 is {divmod(10,3)}")









