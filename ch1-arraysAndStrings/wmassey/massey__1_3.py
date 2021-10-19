#!/usr/bin/env python3
"""project: Cracking the Coding Interview: Chapter 1; Strings & Arrays 
created:2021-09-25, @author:Will Massey, email: wmassey776@gmail.com

Objective:
    URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
    has sufficient space at the end to hold the additional characters, and that you are given the "true"
    length of the string. (Note: If implementing in Java, please use a character array so that you can
    perform this operation in place.) 
"""


def URLify(s):
    s = s.replace(' ', '%20')
    return s


def main():
    print(URLify('Hello World! !!  ')) 
    print(URLify(' Hi  Mrs Jane  Smith. '))    


if __name__ == '__main__':
    main()
    
