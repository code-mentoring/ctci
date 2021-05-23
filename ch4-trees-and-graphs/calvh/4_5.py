def tree_is_bst(tree):

    """
    Problem:
    Implement a function to check if a binary tree is a binary search tree.

    Solution:
    Assume non-empty tree. Perform recursive calls on left and right subtrees.
    """

    def is_bst(node):

        # base case: node with no children
        if node.left is None and node.right is None:
            return True
        elif node.left is None:
            return is_bst(node.right)
        elif node.right is None:
            return is_bst(node.left)
        else:
            return (
                is_bst(node.left)
                and is_bst(node.right)
                and node.left.element <= node.element <= node.right.element
            )

    return is_bst(tree.root)