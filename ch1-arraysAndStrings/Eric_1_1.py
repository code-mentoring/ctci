
# 1.1 - Is Unique Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

import sys

# inputs a string

stringcheck = input("Please enter a string: ")

try:
    val = int(stringcheck)
    print("Input is not a string, it's an integer number. Number = ", val)
    sys.exit()
except ValueError:
    try:
        val = float(stringcheck)
        print("Input is not a string, it's a float number. Number = ", val)
        sys.exit()
    except ValueError:
        print("Input is a valid string")

#initializes variables
check = ''
found = 0

# checks to see if character is in check variable
for i in stringcheck:
    if i in check:
        print("The strong does NOT have unique characters")
        sys.exit()
    check += i

# if the program reaches this point it means there are no repeated characters
print("The string has unique characters")
