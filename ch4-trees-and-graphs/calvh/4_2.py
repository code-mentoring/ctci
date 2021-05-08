def minimum_tree(arr):
    """
    Problem:
    Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

    Strategy:
    A minimum-height tree is a tree that is balanced. The array is sorted so splitting the array in half yield a balanced BST. Start with the root at len(arr)//2, then recurse on both sides.

    Classes:
    Tree(root_node, left_subtree, right_subtree)
    Node(element)
    """

    def construct_tree(left, right):

        if left == right:
            # one element
            return Tree(Node(arr[left]))

        elif right - left == 1:
            # two elements, choose right as root to keep leaves on left side
            return Tree(Node(arr[right]), Tree(Node(arr[left])), None)

        else:
            mid = (left + right) // 2

            return Tree(
                Node(arr[mid]),
                construct_tree(left, mid - 1),
                construct_tree(mid + 1, right),
            )

    return construct_tree(0, len(arr) - 1)