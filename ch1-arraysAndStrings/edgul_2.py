import copy

# 1.6 - compresses all or none - O(n)
def compress(inString : str) -> str:
    current = 0
    l = [] 
    while current < len(inString):
        count = 1
        first = inString[current]
        current+=1
        while current < len(inString) and inString[current] == first:
            count+=1
            current+=1
        l.append(first+str(count))
    output = "".join(l) # O(n)
    if len(output) >= len(inString):
        return inString
    return output

# A slightly smarter compress - O(n)
# Only sequences > 1 will be converted. IE: a -> a, aa -> a2, aab -> a2b
def compress2(inString : str) -> str:
    current = 0
    l = [] 
    while current < len(inString):
        count = 1
        first = inString[current]
        current+=1
        while current < len(inString) and inString[current] == first:
            count+=1
            current+=1
        l.append(first)
        if count > 1:
            l[-1] = first+str(count)
    return "".join(l) # O(n) - faster than concatenation

# helper function - transpose
def transpose(matrix : "NxM list of lists of ints"):
    return [[x[j] for i,x in enumerate(matrix)] for j,y in enumerate(matrix)] 

# 1.7 - Rotate Matrix - rotate matrix by 90deg - O(n^2), which is okay for a matrix
def rotateMatrix(matrix : list) -> list:
    n = len(matrix)
    trans = transpose(matrix)

    # shift
    for i in range(n):
        for j in range(int(n/2)):
            temp = trans[i][j]
            trans[i][j] = trans[i][n-1-j]
            trans[i][n-1-j] = temp
    return trans

# 1.8 - Zero Matrix - clear all rows and columns of found 0 elements 
#     - 0(NxM) for NxM matrix
def zeroMatrix(matrix : 'list of lists') -> 'list of lists':

    # clear row if we find a zero in the row
    rows = copy.deepcopy(matrix) 
    for i,row in enumerate(rows):
        if row.count(0) > 0:
            rows[i] = [0 for x in range(len(rows))]

    # clear col if we find a zero in the col
    columns = transpose(matrix)  
    for j,col in enumerate(columns):
        if col.count(0) > 0:
            columns[j] = [0 for x in range(len(columns))]

    # merge the matrices
    for i, row in enumerate(rows):
        for j,item in enumerate(row):
            rows[i][j] = item and columns[j][i] # note index reversal for columns
    return rows 

def testZeroMatrix():
    # 2x2
    matrix = [[1,2], [3,4]]
    assert zeroMatrix(matrix) == [[1,2], [3,4]]
    matrix = [[0,2], [3,4]]
    assert zeroMatrix(matrix) == [[0,0], [0,4]]
    matrix = [[1,0], [3,4]]
    assert zeroMatrix(matrix) == [[0,0], [3,0]]

    # 3x3
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    assert zeroMatrix(matrix) == [[1,2,3], [4,5,6], [7,8,9]]
    matrix = [[0,2,3], [4,5,6], [7,8,9]]
    assert zeroMatrix(matrix) == [[0,0,0], [0,5,6], [0,8,9]]
    matrix = [[1,0,3], [4,5,6], [7,8,9]]
    assert zeroMatrix(matrix) == [[0,0,0], [4,0,6], [7,0,9]]
    matrix = [[1,2,0], [4,5,6], [7,8,9]]
    assert zeroMatrix(matrix) == [[0,0,0], [4,5,0], [7,8,0]]
    matrix = [[1,2,3], [4,0,6], [7,8,9]]
    assert zeroMatrix(matrix) == [[1,0,3], [0,0,0], [7,0,9]]


def testRotateMatrix():
    matrix = [[1,2], [3,4]]
    assert rotateMatrix(matrix) == [[3,1], [4,2]]
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    assert rotateMatrix(matrix) == [[7,4,1], [8,5,2], [9,6,3]]
    matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    assert rotateMatrix(matrix) == [[13,9,5,1], [14,10,6,2], [15,11,7,3], [16,12,8,4]]

def testCompress():
    assert compress("") == ""
    assert compress("a") == "a"
    assert compress("aa") == "aa"
    assert compress("aaa") == "a3"
    assert compress("aabbcc") == "aabbcc"
    assert compress("aabbccc") == "a2b2c3"
    assert compress("aaabbbccc") == "a3b3c3"
    assert compress("aaaaabbbbbc") == "a5b5c1"
    assert compress("abccc") == "abccc"
    assert compress("abccccc") == "a1b1c5"

def testCompress2():
    assert compress2("") == ""
    assert compress2("a") == "a"
    assert compress2("aa") == "a2"
    assert compress2("aaa") == "a3"
    assert compress2("aabbc") == "a2b2c"
    assert compress2("aabbcc") == "a2b2c2"
    assert compress2("aabbccc") == "a2b2c3"
    assert compress2("aaabbbccc") == "a3b3c3"
    assert compress2("aaaaabbbbbc") == "a5b5c"
    assert compress2("abccc") == "abc3"
    assert compress2("abccccc") == "abc5"

def main():
    testCompress()
    testCompress2()
    testRotateMatrix()
    testZeroMatrix()

main()
