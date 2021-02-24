# 1.7 - Rotate Matrix: 
# Given an image represented by an NxN matrix, where each pixel in the image is an integer, 
# write a method to rotate the image by 90 degrees. Can you do this in place?

# Example 3x3 matrix:
#
#    j1 j2 j3
#     _ _ _
# i1 |1 2 3
# i2 |4 5 6
# i3 |7 8 9
#
# Rows are horizontal lines and columns are vertical lines,
# so the first row (i=0) consists of [1,2,3] and the first column (j=0) consists
# of [1,4,7].
#
# Rotating the above matrix 90 degrees anti-clockwise would switch columns with rows as follows:
#    _ _ _
#   |3 6 9
#   |2 5 8
#   |1 4 7
#
# Approach has two main steps, transpose and flip:
# 1. Transpose, i.e. swap(matrix[i][j], matrix[j][i]) making the rows as columns and columns as rows. 
# 2. Flip on vertical or horizontal axis for clockwise or anticlockwise rotation, respectively. 
#    vertical -> swap(matrix[i][j], matrix[i][N-1-j]
#    horizontal -> swap(matrix[i][j], matrix[N-1-i][j]
#
# E.g. flip first row after transpose using 'N-1-j':
#   1 (i0, j0): 3-1-0 = 2  --> (i0, j2) 7
#   4 (i0, j1): 3-1-1 = 1  --> (i0, j1) 4
#   7 (i0, j2): 3-1-2 = 0  --> (i0, j0) 1
#
# Two-dimensional list can represent a matrix in python.

def rotate(original_matrix):
    num_columns = len(original_matrix[0])
    num_rows = len(original_matrix)
    print(f"Rotating {num_rows}x{num_columns} matrix.")

    transposed_matrix = transpose(original_matrix, num_rows, num_columns)

    return transposed_matrix

# Transpose, i.e. swap(matrix[i][j], matrix[j][i]) making the rows as columns and columns as rows. 
def transpose(matrix, num_rows, num_columns):
    # Copy whole matrix to know the dimensions, but values will be transposed.
    transposed_matrix = matrix.copy()
    # TODO: use https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

    # Traversal hits every element of multi-dimensional structure using nested loop.
    # TODO: Avoid duplicate swaps.
    for row in range(num_rows):

        print(f"row: {row}")
        print("current transpose:")
        for r in transposed_matrix:
            print(r)

        for col in range(num_columns):
            if (row != col):
                print(col)
                print(f"setting {transposed_matrix[row][col]} to {matrix[col][row]}")
                transposed_matrix[row][col] = matrix[col][row]

    return transposed_matrix  

def flip_vertical(matrix):
    flipped_matrix = None

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print("original matrix:")
for row in matrix:
    print(row)

rotated_matrix = rotate(matrix)
print("rotated matrix:")
for row in rotated_matrix:
    print(row)