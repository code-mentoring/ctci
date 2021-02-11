
# 1.1 - Is Unique - (Uses set) - O(n)
def isUnique(someStr : str) -> bool:
    myset = set() 
    for c in someStr:
        if c in myset:
            return False
        myset.add(c) 
    return True;

# 1.1 - Is Unique (no data structure) - O(n^2)
def isUniqueSlow(someStr : str) -> bool:
    for i in range(len(someStr)):
        for j in range(i+1, len(someStr)):
            if (someStr[i] == someStr[j]):
                return False
    return True

# 1.2 - checkPermutation - O(n+m) where m is number of unique elements
def checkPermutation(str1 : str, str2 : str):
    # quick check
    if len(str1) != len(str2):
        return False

    # build two dictionaries of characters
    myDict1 = dict()
    myDict2 = dict()
    for i in range(len(str1)):
        c1 = str1[i]
        if myDict1.get(c1) == None:
            myDict1[c1] = 0
        myDict1[c1] += 1
        
        c2 = str2[i]
        if myDict2.get(c2) == None:
            myDict2[c2] = 0
        myDict2[c2] += 1
  
    # verify each dictionary matches in counts
    for c in myDict1:
        if myDict1.get(c) != myDict2.get(c):
            return False
    return True
       
# 1.4 - Palindrome permutation

# 1.1 - Test function
def testIsUnique(someUniqueFunc):
   print(someUniqueFunc("") == True)
   print(someUniqueFunc("x") == True)
   print(someUniqueFunc("xx") == False)
   print(someUniqueFunc("xyx") == False)
   print(someUniqueFunc("abcdefghijklmnop") == True)
   print(someUniqueFunc("AabcdefghijklmnopaA") == False)

# 1.2 - Test function
def testCheckPermutation():
    print(checkPermutation("a", "a") == True)
    print(checkPermutation("a", "aa") == False)
    print(checkPermutation("aa", "a") == False)
    print(checkPermutation("aa", "aa") == True)
    print(checkPermutation("a", "b") == False)
    print(checkPermutation("abcd", "dcba") == True)
    print(checkPermutation("aaa", "aaa") == True)
    print(checkPermutation("aaa", "aa") == False)


# testIsUnique(isUnique)
testCheckPermutation()
