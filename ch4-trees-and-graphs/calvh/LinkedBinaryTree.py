class LinkedBinaryTree:
    def __init__(self, root=None):
        self.root = root

    def is_external(self, node):
        return node.left is None and node.right is None

    def height(self, node):
        if self.is_external(node):
            return 0

        h = max(self.height(node.left), self.height(node.right))

        return h + 1