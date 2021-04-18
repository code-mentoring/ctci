# 1.8 - Zero Matrix: 
# Write an algorithm such that if an element in an MxN matrix is 0, 
# its entire row and column are set to 0.
#
# E.g. this:
#    _  _  _ _
#   |1  2  3 4
#   |5  0  7 8
#   |9 10 11 12
#
# would become:
#     _ _  _ _
#   |1  0  3 4
#   |0  0  0 0
#   |9  0 11 12

def get_zero_matrix(matrix):
    zero_matrix = []
    column_index_to_be_zero = set() # Use Set to avoid duplicates.

    zero_the_rows(matrix, zero_matrix, column_index_to_be_zero)
    zero_the_columns(zero_matrix, column_index_to_be_zero)

    return zero_matrix

def zero_the_rows(matrix, zero_matrix, column_index_to_be_zero):
    num_columns = len(matrix[0])
    for row in matrix:
        row_has_zero = False
        for column_index in range(num_columns):
            if (row[column_index] == 0):
                row_has_zero = True 
                column_index_to_be_zero.add(column_index)
        if (row_has_zero):
            zero_row = [0] * num_columns # Create new object each time.
            zero_matrix.append(zero_row)
        else:
            zero_matrix.append(row) 

def zero_the_columns(zero_matrix, column_index_to_be_zero):
    for column_index in column_index_to_be_zero:
        for row in zero_matrix:
            row[column_index] = 0

# Testing.
matrix = [[1,2,3,4,3], [5,4,7,8,3], [9,0,11,12,3], [13,14,15,3,3]]
#matrix = [[1,0,0], [4,5,6], [7,8,0]]
#matrix = [[1,2,3,4,3], [5,0,7,8,3], [9,0,11,12,3], [13,14,15,0,3]]
print("original matrix:")
for row in matrix:
    print(row)

zero_matrix = get_zero_matrix(matrix)
print("zero matrix:")
for row in zero_matrix:
    print(row)