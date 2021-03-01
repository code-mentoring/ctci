# /**
#  * @author [Mohamad Jayyusi]
#  * @email 
#  * @create date 2021-02-23
#  * @modify date 2021-02-23
#  * @desc 1.8 - Zero Matrix: Write an algorithm such that if an element in an MxN
#                matrix is 0, its entire row and column are set to 0.
#  */

#set matrix dimension
m = 4
n = 5
#value to fill matrix with
initialValue = 7
matrix = []
zeroIndices = []

#set a cell to 0 - O(1) time complexity
def setZero(i, j):
    matrix[i][j] = 0

#print matrix - O(n) time complexity
def printMatrix():
    for i in range(0,m):
        print(matrix[i])

#create matrix - O(n) time complexity
def createMatrix():
    for i in range(0,m):
        matrix.append([ initialValue ] * n) #O(n) time complexity

#initialize uni dimensional array
#for storing indices of zero cells
#O(n²) time complexity
def zeroIndicesArray():
    for i in range(0,m):
        for j in range(0, n):
          zeroIndices.append(initialValue)

#locate zero cells
#O(n²) time complexity
def findZeroIndices():
    for i in range(0,m):
        for j in range(0, n):
          if matrix[i][j] == 0:
              zeroIndices[i*n+j] = 0

#zero rows and cols
#O(n) time complexity
def setRowAndColToZeros(rowNum, colNum):
    for j in range(0,n):
        setZero(rowNum, j)
    
    for i in range(0,m):
        setZero(i, colNum)

#zero matrix O(n²)
def zeroMatrix():
    for i in range(0,len(zeroIndices)):
        if zeroIndices[i] == 0:
            setRowAndColToZeros(i//n,i%n)

# Solution
createMatrix()
zeroIndicesArray()
printMatrix()
print() # blank line
# setZero(0,0)
setZero(1,1)
# setZero(2,2)
findZeroIndices()
zeroMatrix()
printMatrix()