import unittest

from ctci.BinaryTreeNode import BinaryTreeNode as Node


def merge_permutations(p1, p2):
    """
    returns a list of all possible permutations of p1 merged with p2
    while perserving the relative order of the elements in p1 and p2

    example:
    p1: [1,2]
    p2: [3,4]

    output:
    [
        [1,2,3,4]
        [1,3,2,4]
        [1,3,4,2]
        [3,1,2,4]
        [3,1,4,2]
        [3,4,1,2]
    ]
    """

    permutations = []

    # base case
    if len(p2) == 1:
        for position in range(len(p1) + 1):
            permutations.append(p1[:position] + [p2[0]] + p1[position::])
    else:
        for position in range(len(p1) + 1):
            for p in merge_permutations(p1[position::], p2[1::]):
                permutations.append(p1[:position] + [p2[0]] + p)
    return permutations


def bst_sequences(start):

    """
    Problem:
    A binary search tree was created by traversing through an array from left to right and inserting each element.
    Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

    EXAMPLE:

    Input:
    2 -> 1
    2 -> 3

    Output: {2, 1, 3}, {2, 3, 1}

    """

    arrays = []

    if start is None:
        return []

    if start.left is None and start.right is None:
        arrays.append([start.element])

    elif start.left is None:
        for r_p in bst_sequences(start.right):
            arrays.append([start.element] + r_p)

    elif start.right is None:
        for l_p in bst_sequences(start.left):
            arrays.append([start.element] + l_p)

    else:
        # combine permutations from left and right subtrees in all possible ways
        for l_p in bst_sequences(start.left):
            for r_p in bst_sequences(start.right):
                for p in merge_permutations(l_p, r_p):
                    arrays.append([start.element] + p)

    return arrays


class TestBSTSequences(unittest.TestCase):
    def test_case_0(self):
        """
            2
        1       3
        """
        btnroot = Node(2)
        btn1 = Node(1)
        btn3 = Node(3)
        btnroot.left = btn1
        btnroot.right = btn3

        for row in bst_sequences(btnroot):
            print(row)

    def test_case_1(self):
        """
        0
            1
                2

        """
        btnroot = Node(0)
        btn1 = Node(1)
        btn2 = Node(2)
        btnroot.right = btn1
        btn1.right = btn2

        for row in bst_sequences(btnroot):
            print(row)

    def test_case_2(self):
        """
                    5
            2               8
        1       4
        """
        btnroot = Node(5)
        btn1 = Node(1)
        btn2 = Node(2)
        btn4 = Node(4)
        btn5 = Node(5)
        btn8 = Node(8)
        btnroot.left = btn2
        btnroot.right = btn8
        btn2.left = btn1
        btn2.right = btn4

        for row in bst_sequences(btnroot):
            print(row)

    def test_case_3(self):
        """
                    4
            2               6
        1       3       5       7

        """

        btnroot = Node(4)
        btn1 = Node(1)
        btn2 = Node(2)
        btn3 = Node(3)
        btn5 = Node(5)
        btn6 = Node(6)
        btn7 = Node(7)
        btnroot.left = btn2
        btnroot.right = btn6
        btn2.left = btn1
        btn2.right = btn3
        btn6.left = btn5
        btn6.right = btn7

        for row in bst_sequences(btnroot):
            print(row)


if __name__ == "__main__":
    unittest.main()
