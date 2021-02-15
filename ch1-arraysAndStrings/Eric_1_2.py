
# I'm not used to doing coding challenges, so please go easy on me!  lol

# 1.2 - Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

# Note: for all of my solutions, you can run the program and it will then ask you to input the required strings

import sys

class functionforinputString: 
    def __init__(self,string1, string2):
        self.string1 = string1
        self.string2 = string2
    def rotate(self):
        if len(self.string1) == len(self.string2) and self.string2 in self.string1*2:
            print(self.string2,"is a permutation of",self.string1)
        else:
            print(self.string2,"is NOT a permutation of",self.string1)
    def checkstring(self, stringcheck):
        try:
            int(stringcheck)
            print(stringcheck,"is not a string, it's an integer")
            sys.exit()
        except ValueError:
            try:
                float(stringcheck)
                print(stringcheck,"is not a string, it's a float")
                sys.exit()
            except ValueError:
                pass


comparing = functionforinputString(input("Please enter string #1: "),input("Please enter string #2: "))
comparing.checkstring(comparing.string1)
comparing.checkstring(comparing.string2)
comparing.rotate()

