# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:57:53 2021

@author: clark

.1 - Is Unique Implement an algorithm to determine if a string has all unique 
characters. What if you cannot use additional data structures?
"""

def checkUnique (str):
    for cha in str:
        if str.count(cha) > 1:
            return False
    
    return True



print(checkUnique("abcdefg_56"))
print(checkUnique("__abcdefg"))
print(checkUnique("abcdddefg"))