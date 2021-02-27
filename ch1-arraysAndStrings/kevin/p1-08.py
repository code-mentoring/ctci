"""
1.8 - Zero Matrix:
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""

def with_zeroed_rows(A):
    new_A = []
    for row in A:
        if 0 in row:
            new_A.append([0 for _ in row])
        else:
            new_A.append(row[:])
    return new_A

def main():
    cases = [
        ([], []),
        ([[1,0,1],[1,3,9]], [[0,0,0],[1,3,9]]),
    ]
    for A, expected in cases:
        actual = with_zeroed_rows(A)
        print("[" + ("PASS" if actual == expected else "FAIL") + "]",
              A,
              expected,
              actual)

if __name__ == "__main__":
    main()
