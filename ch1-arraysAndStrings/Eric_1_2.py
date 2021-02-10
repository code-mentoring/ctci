
# 1.2 - Check Permutation Given two strings, write a method to decide if one is a permutation of the other.

import sys

def checkstring(stringcheck):
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


string1 = input("Please enter string 1: ")
string2 = input("Please enter string 2: ")

checkstring(string1)
checkstring(string2)

