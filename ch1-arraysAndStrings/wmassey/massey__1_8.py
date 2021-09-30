#!/usr/bin/env python3
"""project: Cracking the Coding Interview: Chapter 1; Strings & Arrays 
created:2021-09-25, @author:Will Massey, email: wmassey776@gmail.com

Objective:
    Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
    column are set to 0.
"""


def zero_matrix(m):
    for row in m:
        for i, col in enumerate(row):
            if col == 0:
                m[1- i].pop()
                for i in range(len(row)-1):
                    m[i-1] = [0]
 
  
    return m


def main():
    print(zero_matrix(([[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]])))
  
    

if __name__ == '__main__':
    main()