"""
1.1 - Is Unique
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?

1.2 - Check Permutation
Given two strings, write a method to decide if one is a permutation of the other.

1.4 - Palindrome Permutation
Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

"""
#Question 1.1 - Is Unique
#Question 1.2 - Check Permutation

#Question 1.4 - Palindrome Permutation
def IsPalindrome ( S ) :
    start = 0
    end = len ( S ) -1
    while start < end :
        if S [start] != S [end] :
            return False
        start +=1
        end -= 1
            
    return True