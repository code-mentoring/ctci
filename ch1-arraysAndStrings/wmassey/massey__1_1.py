#!/usr/bin/env python3
"""project: Cracking the Coding Interview: Chapter 1; Strings & Arrays 
created:2021-09-25, @author:Will Massey, email:seraph776@gmail.com"""



def main():
    print(is_uniqe('hello'))
    print(is_uniqe('world')) 

    
def is_uniqe(s: str) -> str:
    return (len(set(s))) == len(s)



if __name__ == '__main__':
    main()
    
