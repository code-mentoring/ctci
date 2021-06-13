class BinaryTreeNode:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self is other

    def __ne__(self, other):
        return self.element != other.element

    def __lt__(self, other):
        return self.element < other.element

    def __le__(self, other):
        return self.element <= other.element

    def __gt__(self, other):
        return self.element > other.element

    def __ge__(self, other):
        return self.element >= other.element

    def __repr__(self):
        return f"{self.element}"