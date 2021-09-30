#!/usr/bin/env python3
"""project: Cracking the Coding Interview: Chapter 1; Strings & Arrays 
created:2021-09-25, @author:Will Massey, email: wmassey776@gmail.com

Objective:
    Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
    A palindrome is a word or phrase that is the same forwards and backwards. A permutation
    is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words
"""


def is_uniqe(s: str) -> bool:
    return (len(set(s))) == len(s)


def main():
    print(is_uniqe('hello'))
    print(is_uniqe('bird'))    
    

if __name__ == '__main__':
    main()