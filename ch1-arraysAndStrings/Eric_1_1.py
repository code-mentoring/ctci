
# I'm not used to doing coding challenges, so please go easy on me!  lol

# 1.1 - Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# Note: for all of my solutions, you can run the program and it will then ask you to input the required strings

import sys

# inputs a string
stringcheck = input("Please enter a string: ")

# Checks to make sure input is a valid string
try:
    val = int(stringcheck)
    print(stringcheck,"is not a string, it's an integer")
    sys.exit()
except ValueError:
    try:
        val = float(stringcheck)
        print(stringcheck,"is not a string, it's a float")
        sys.exit()
    except ValueError:
        pass

# initializes variables - check will be used to keep a running count of the characers in the input string
check = ''
found = 0

# Checking to see if the string shows up more than once
for i in stringcheck:
    if i in check:
        print("The strong does NOT have unique characters")
        sys.exit()
    check += i

# if the program reaches this point it means there are no repeated characters
print("The string has unique characters")
