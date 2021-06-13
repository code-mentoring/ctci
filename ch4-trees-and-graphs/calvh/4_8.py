import unittest


from ctci.BinaryTreeNode import BinaryTreeNode as Node


def first_common_ancestor(root, node1, node2):

    """
    Problem:
    Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
    Avoid storing additional nodes in a data structure.
    NOTE: This is not necessarily a binary search tree.
    NOTE: An ancestor can be the node itself.

    """

    if root == node1 or root == node2:
        return root

    def find_fca(current, node1, node2):

        if current is None:
            return 0

        current_node_matches = current == node1 or current == node2
        left = find_fca(current.left, node1, node2)
        right = find_fca(current.right, node1, node2)

        # answer already found, return upwards
        if isinstance(left, Node):
            return left

        if isinstance(right, Node):
            return right

        # answer found
        if current_node_matches + left + right == 2:
            return current

        return current_node_matches + left + right

    return find_fca(root, node1, node2)


class TestFca(unittest.TestCase):
    def test_solution(self):
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

        input_values = [(0, 1), (0, 2), (7, 8), (1, 2), (7, 14), (3, 11), (7, 10)]
        expected_values = [0, 0, 3, 0, 0, 0, 1]

        for value, expected in zip(input_values, expected_values):
            with self.subTest(nodes=(value), answer=expected):
                self.assertEqual(
                    first_common_ancestor(
                        nodes[0], nodes[value[0]], nodes[value[1]]
                    ).element,
                    expected,
                )


if __name__ == "__main__":
    unittest.main()