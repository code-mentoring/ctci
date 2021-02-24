
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

# 1.7 - Rotate Matrix - rotate matrix by 90deg - O(n^2), which is okay for a matrix
def rotateMatrix(matrix : list) -> list:
    n = len(matrix)

    # transpose
    transpose = [[0 for y in matrix[0]] for x in matrix]
    for i in range(n):
        for j in range(n):
            transpose[i][j] = matrix[j][i]

    # shift
    for i in range(n):
        for j in range(int(n/2)):
            temp = transpose[i][j]
            transpose[i][j] = transpose[i][n-1-j]
            transpose[i][n-1-j] = temp
    return transpose

# 1.8 - Zero Matrix - clear row and column of found 0 element
def zeroMatrix(matrix : list) -> list:
    pass

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

main()
