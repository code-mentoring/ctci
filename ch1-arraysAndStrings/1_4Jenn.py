# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:45:03 2021

@author: clark

1.4 - Palindrome Permutation
Given a string, write a function to check if it is a permutation of a 
palindrome. A palindrome is a word or phrase that is the same forwards and 
backwards. A permutation is a rearrangement of letters. The palindrome does 
not need to be limited to just dictionary words. 
"""

def checkPermPalindrome(str0):
    if len(str0)%2 == 0:
        for ch in str0:
            num = str0.count(ch)
            if num%2 == 1:
                return False
            
        return True
    else:
       oddNum = 0
       charList = [];
       
       for ch in str0:
           if charList.count(ch) == 0:
               charList.append(ch)
       
       for x in charList:
           if str0.count(x)%2 == 1:
               oddNum = oddNum + 1
               
       if oddNum > 1:
           return False
       else:
           return True
       
           
    
print(checkPermPalindrome("abccbax"))
print(checkPermPalindrome("asd457fgh"))