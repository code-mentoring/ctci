#!/usr/bin/env python3
"""project: Cracking the Coding Interview: Chapter 1; Strings & Arrays 
created:2021-09-25, @author:Will Massey, email: wmassey776@gmail.com

Objective:
    Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
    is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""
from itertools import permutations as perm


def palindrome_permutation(s) -> bool:
    s = s.lower()

    # Permute string 's'
    permuted_string = list(perm(s))
    for letter_combo in permuted_string:
        new_word = ''.join(letter_combo)
        if new_word == new_word[::-1]:
        #print(new_word, new_word[::-1])  # (WTFO!): Not producing permutation "taco cat", "atco eta"
            return new_word, new_word[::-1]
    return False


def main():
    print(palindrome_permutation('Tact Coa'))
  
    
if __name__ == '__main__':
    main()