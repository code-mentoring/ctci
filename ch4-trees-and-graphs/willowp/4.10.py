class BinaryTree:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def subtree(a, b):
  if b is None:
    return True
  elif a is None:
    return False

  if a.val == b.val and match(a, b):
    return True

  return subtree(a.left, b) or subtree(a.right, b) or False

def match(a, b):
  if a is None and b is None:
    return True
  if a and b and a.val == b.val:
    return match(a.left, b.left) and match(a.right, b.right)
  return False

tree_a = BinaryTree(1)
tree_b = BinaryTree(1)
print(subtree(tree_a, tree_b) is True)
tree_c = BinaryTree(2)
print(subtree(tree_a, tree_c) is False)
tree_a.left = tree_c
print(subtree(tree_a, tree_c) is True)
print(subtree(tree_a, tree_b) is False)
tree_d = BinaryTree(2)
print(subtree(tree_a, tree_d) is True)
tree_c.right = tree_b
print(subtree(tree_a, tree_c) is True)
big_root = BinaryTree(1)
big_root.left = BinaryTree(2)
big_root.right = BinaryTree(100)
big_root.left.right = BinaryTree(3)
big_root.right.left = BinaryTree(200)
big_root.right.right = BinaryTree(200)
big_root.left.left = BinaryTree(4)

print(subtree(big_root, big_root.right) is True)
