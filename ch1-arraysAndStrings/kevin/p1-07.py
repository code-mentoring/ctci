"""
1.7 - Rotate Matrix:
Given an image represented by an NxN matrix, where each pixel in the image is an integer, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotate_smart_arse(A):
    # The smart-arse solution.
    return list(map(list, zip(*reversed(A))))

def rotate_in_place(A):
    # The in-place solution.
    # Phase 1: transpose the matrix.
    # Swap the element at position i,j with the one at j,i.
    # Since that's the definition of transposition.
    # Diagonal remains the same since i=j.
    for i in range(1, len(A)):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    # Phase 2: reverse the rows.
    for row in A:
        for i in range(len(row)):
            swap_index = len(row)-i-1
            if swap_index <= i:
                break
            row[i], row[swap_index] = row[swap_index], row[i]

def main():
    cases = [
        ([[1,2],[3,4]], [[3,1],[4,2]]),
        ([[1]], [[1]]),
        ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
    ]
    for A, expected in cases:
        # Make a copy so that we don't corrupt the original.
        actual = [row[:] for row in A]
        rotate_in_place(actual)
        print("[" + ("PASS" if actual == expected else "FAIL") + "]",
              A,
              expected,
              actual)

if __name__ == "__main__":
    main()
