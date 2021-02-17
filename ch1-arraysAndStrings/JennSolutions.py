# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:23:41 2021

@author: clark

1.6 - String Compression: Implement a method to perform basic string compression 
using the counts of repeated characters. For example, the string a a b c c c c c a a a
 would become a 2 b l c 5 a 3 , If the "compressed" string would not become 
 smaller than the original string, your method should return the original string. 
 You can assume the string has only uppercase and lowercase letters (a - z).

1.7 - Rotate Matrix: Given an image represented by an NxN matrix, where each 
pixel in the image is an integer, write a method to rotate the image by 90 
degrees. Can you do this in place?

1.8 - Zero Matrix: Write an algorithm such that if an element in an MxN matrix 
is 0, its entire row and column are set to 0.
"""

def compress(str0):
    sep = ""
    
    for x in range(len(str0)):
        if (x == 0):
            sep = sep + str0[x]
        elif (str0[x] == str0[x - 1]):
            sep = sep + str0[x]
        else:
            sep = sep + "-" + str0[x]
    
    lst = sep.split("-")
    com = []
    
    for s in lst:
        x = s[0] + str(len(s))
        com.append(x)
        
    output = ""
    
    for s in com:
        output = output + s
        
    if (len(output) > len(str0)):
        return str0
    else:
        return output
       


"""
Assume the NXN matrix is a list of lists.

1.7 - Rotate Matrix: Given an image represented by an NxN matrix, where each 
pixel in the image is an integer, write a method to rotate the image by 90 
degrees. Can you do this in place?
"""

def rotate1(mtx):
    output = []
    
    for x in range(len(mtx)):
        line = []
        
        for y in range(len(mtx)):
            line.append(mtx[y][x])

        output.insert(0, line)
        
    return output


"""
But wait, we have matrixs of intergers, so I can use matrix multiplication and
the rotation transfromation? I don't think we can.
"""

def zeroMtx(mtx):
    colums = []
    rows = []
    
    for x in range(len(mtx)):
        for y in range(len(mtx[x])):
            if mtx[x][y] == 0:
                if colums.count(x) == 0:
                    colums.append(x)
                    
                if rows.count(y) == 0:
                    rows.append(y)
                    
    for e in colums:
        for x in range(len(mtx[0])):
            mtx[e][x] = 0
            
    for e in rows:
        for x in range(len(mtx)):
            mtx[x][e] = 0
            
    return mtx
                    
    
    
    

            
    