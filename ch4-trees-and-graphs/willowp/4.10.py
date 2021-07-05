class BinaryTree:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

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

big = BinaryTree(1,
  BinaryTree(2,
    BinaryTree(3),
    BinaryTree(3)),
  BinaryTree(5,
    BinaryTree(4),
    BinaryTree(9))
  )
small = BinaryTree(2,
    BinaryTree(3),
    BinaryTree(3))

print(subtree(big, small) is True)

big2 = BinaryTree(1,
  BinaryTree(2,
    BinaryTree(3),
    BinaryTree(3)),
  BinaryTree(5,
    BinaryTree(4),
    BinaryTree(9))
  )
small2 = BinaryTree(3,
    BinaryTree(3),
    BinaryTree(2))

print(subtree(big2, small2) is False)

big3 = BinaryTree(1,
  BinaryTree(2,
    BinaryTree(3),
    BinaryTree(3, BinaryTree(5))),
  BinaryTree(5,
    BinaryTree(4),
    BinaryTree(9))
  )
small3 = BinaryTree(2,
    BinaryTree(3),
    BinaryTree(3))

print(subtree(big3, small3) is False)
