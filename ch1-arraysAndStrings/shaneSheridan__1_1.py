# 1.1 - Is Unique
# Implement an algorithm to determine if a string has all unique characters, without 
# using additional data structures.

# Sort a given string and simply compare each character to the next one.
def isUnique(s):
    s = sorted(s)
    for i in range(len(s)-1):
        if (s[i] == s[i+1]):
            return False
    return True

# Test.
someStrings = ["apple", "banana", "cherry", "tuna", "12345", "123445", "he!!0", "he123", "he1233"]
for s in someStrings:
    print(f"Checking if '{s}' is unique.")
    print(isUnique(s)) 