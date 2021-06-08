import unittest

from ctci.BinaryTreeNode import BinaryTreeNode as Node
from ctci.LinkedBinaryTree import LinkedBinaryTree as BT
from ctci.LinkedBinarySearchTree import LinkedBinarySearchTree as BST


def tree_is_bst(tree):

    """
    Problem:
    Implement a function to check if a binary tree is a binary search tree.

    Solution:
    Assume non-empty tree. Assume BSTs can have no duplicates.
    Perform recursive calls on left and right subtrees.
    """

    def is_bst(current):

        left = current.left
        right = current.right

        # base case: node with no children
        if left is None and right is None:
            return True
        elif left is None:
            return (current < right) and is_bst(right)
        elif right is None:
            return (left < current) and is_bst(left)
        else:
            return left < current < right and is_bst(left) and is_bst(right)

    return is_bst(tree.root)


class TestIsBST(unittest.TestCase):
    def test_is_bst_0(self):
        """
                                    0
                    1                               2

            3               4               5              6

        7       8       9       10      11      12      13      14

        """
        nodes = [Node(i) for i in range(15)]

        for n in range(7):
            nodes[n].left = nodes[2 * n + 1]
            nodes[n].right = nodes[2 * n + 2]

        not_bst = BT(nodes[0])

        self.assertEqual(tree_is_bst(not_bst), False)

    def test_is_bst_1(self):
        """
                                    7
                    3                               8

            2               4

        1

        """
        bst_tree = BST()

        for n in [7, 3, 8, 2, 4, 1]:
            bst_tree.add(Node(n))

        self.assertEqual(tree_is_bst(bst_tree), True)


if __name__ == "__main__":
    unittest.main()
