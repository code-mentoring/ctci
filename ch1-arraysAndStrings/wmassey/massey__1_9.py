#!/usr/bin/env python3
"""project: Cracking the Coding Interview: Chapter 1; Strings & Arrays 
created:2021-09-25, @author:Will Massey, email: wmassey776@gmail.com

Objective:
    String Rotation:Assumeyou have a method isSubstringwhich checks if oneword is a substring
    of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
    call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat"). 
"""
import string

def string_rotation(s1, s2):
    # If strinsg are not equal length return False:
    if len(s1) != len(s2):
        return False
    
    # Change string to list:
    s1 = list(s1)
    
    # For length of s1, rotate completly: 
    for i in range(len(s1)-1):       
        s1.append(s1.pop(0))  
        # If a match return True   
        if ''.join(s1) == s2:
            return True      
    return False

def main():
    print(string_rotation('waterbottle', 'erbottlewat'))
    print(string_rotation('watertables', 'erbottlewat'))



if __name__ == '__main__':
    main()