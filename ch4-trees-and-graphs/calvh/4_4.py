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
        elif node.left is None:
            return is_balanced(node.right)
        elif node.right is None:
            return is_balanced(node.left)
        else:
            return (
                is_balanced(node.left)
                and is_balanced(node.right)
                and abs(tree.height(node.left) - tree.height(node.right)) <= 1
            )

    return is_balanced(tree.root)
