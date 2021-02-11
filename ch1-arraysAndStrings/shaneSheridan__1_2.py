# 1.2 - Check Permutation 
# Given two strings, write a method to decide if one is a permutation of the other.
# E.g. “abcd” is a permutation of “dabc”.

# TODO: a permutation is a rearrangement of letters so are identical strings NOT 
# permutations since there's no rearrangement?

# Permuation strings must be:
# 1. the same lenth.
# 2. identical when sorted, but not initially (see TODO above), and assuming case sensitivity here. 
def is_permutation(s1, s2):
    s1Len = len(s1)
    s2Len = len(s2)
    if (s1Len != s2Len):
        return False
    
    s1 = sorted(s1)
    s2 = sorted(s2)
    if (is_identical(s1, s2)):
        return True
    
    return False

def is_identical(s1, s2):
    return True if (s1==s2) else False

# Test.
some_strings = [["abcd", "dabc"], ["abcd", "erf"], ["abcd", "erfg"], ["abcd", "abcd"], ["abcd", "DaBc"], ["aBcD", "DaBc"], ["abcd", "DaBc "], ["ab cd", "dabc "]]
for s in some_strings:
    s1 = s[0]
    s2 = s[1]
    print(f"Checking if '{s1}' is a permutation of '{s2}'.")
    print(is_permutation(s1, s2)) 