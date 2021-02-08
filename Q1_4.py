# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:12:55 2021

@author: clark

 Check Permutation Given two strings, write a method to decide if one is a 
 permutation of the other.
"""

def checkPermutation (str1, str2):
        
    def listFromString(str0):
        output = []
        for x in str0:
            output.append(x)
            
        return output
    
    l1 = listFromString(str1)
    l2 = listFromString(str2)
    
    l1.sort()
    l2.sort()
    
    if len(l1) != len(l2):
        return False
    else:
        for x in range(len(l1)):
            if l1[x] != l2[x]:
                return False
        
    return True
    


print(checkPermutation("abcde", "bdcea"))
print(checkPermutation("ab", "bdcea"))  
print(checkPermutation("abcde", "bdc23"))  
print(checkPermutation("abcxy", "bdcea"))    