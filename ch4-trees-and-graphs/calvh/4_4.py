import unittest

from ctci.BinaryTreeNode import BinaryTreeNode as Node
from ctci.LinkedBinaryTree import LinkedBinaryTree as Tree


def tree_is_balanced(tree):

    """
    Problem:
    Implement a function to check if a binary tree is balanced. For the purposes of
    this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
    node never differ by more than one.

    Solution:
    Assume non-empty tree. Perform recursive calls on left and right subtrees.
    """

    def is_balanced(node):

        # base case: node with no children
        if node.left is None and node.right is None:
            return True

        if node.left is None:
            return is_balanced(node.right)

        if node.right is None:
            return is_balanced(node.left)

        return (
            is_balanced(node.left)
            and is_balanced(node.right)
            and abs(tree.height(node.left) - tree.height(node.right)) <= 1
        )

    return is_balanced(tree.root)


class TestIsBalanced(unittest.TestCase):
    def setUp(self):

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

        tree = Tree(nodes[0])

        self.nodes = nodes
        self.tree = tree

    def test_height(self):
        input_values = [0, 1, 3, 7]
        expected_values = [3, 2, 1, 0]

        for value, expected in zip(input_values, expected_values):
            with self.subTest(node=value):
                self.assertEqual(self.tree.height(self.nodes[value]), expected)

    def test_is_balanced_0(self):
        self.assertEqual(tree_is_balanced(self.tree), True)

    def test_is_balanced_1(self):
        """
                                    0
                    1                               2

            3               4

        7       8       9       10

        """
        new_nodes = [Node(i) for i in range(15)]

        for n in [0, 1, 3, 4]:
            new_nodes[n].left = new_nodes[2 * n + 1]
            new_nodes[n].right = new_nodes[2 * n + 2]

        unbalanced_tree = Tree(new_nodes[0])

        self.assertEqual(tree_is_balanced(unbalanced_tree), False)


if __name__ == "__main__":
    unittest.main()
