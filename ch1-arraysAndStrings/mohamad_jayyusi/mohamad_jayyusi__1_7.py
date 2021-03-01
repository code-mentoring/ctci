# /**
#  * @author [Mohamad Jayyusi]
#  * @email 
#  * @create date 2021-02-24
#  * @modify date 2021-02-24
#  * @desc 1.7 - Rotate Matrix: Given an image represented by an NxN matrix, where
#  *       each pixel in the image is an integer, write a method to rotate the
#  *       image by 90 degrees. Can you do this in place?
#  */

n = 5

matrix = [
            [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ],
            [ 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ], [ 31, 32, 33, 34, 35, 36, 37, 38, 39, 40 ],
            [ 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 ], [ 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 ],
            [ 61, 62, 63, 64, 65, 66, 67, 68, 69, 70 ], [ 71, 72, 73, 74, 75, 76, 77, 78, 79, 80 ],
            [ 81, 82, 83, 84, 85, 86, 87, 88, 89, 90 ], [ 91, 92, 93, 94, 95, 96, 97, 98, 99, 100 ]
        ]

result = []

for i in range(n):
    #matrix.append([i] * n)
    result.append([i] * n)

def printMatrix(arr):
    for i in range(n):
        print(arr[i])

# rotate right 90°
def rotateRight90():
    for i in range(0,n):
        x = n-1
        for j in range(0,n):
            result[i][j] = matrix[x][i]
            x = x-1

printMatrix(matrix)
print()
rotateRight90()
print()
printMatrix(result)