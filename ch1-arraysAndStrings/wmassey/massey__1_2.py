#!/usr/bin/env python3
"""project: Cracking the Coding Interview: Chapter 1; Strings & Arrays 
created:2021-09-25, @author:Will Massey, email: wmassey776@gmail.com

Objective:
    Check Permutation: Given two strings, write a method to decide if one is 
    a permutation of the other. 
"""


def check_permutation(s1: str, s2: str) -> str:
    if len(s1) != len(s2):
        return False

    # Sort list and compare each value
    s1 = ''.join([i for i in sorted(s1)])
    s2 = ''.join([i for i in sorted(s2)])

    # Compare each letter in sorted list
    for letterA, letterB in list(zip(s1, s2)):
        if letterA != letterB:
            return False
    return True


def main():
    print(check_permutation('python', 'optynh'))
    print(check_permutation('programming', 'mroggraipmn'))
    print(check_permutation('!ocsrk', 'rocks!'))
    print(check_permutation('javascript', 'bytes'))




if __name__ == '__main__':
    main()