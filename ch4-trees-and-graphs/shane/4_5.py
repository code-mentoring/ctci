# 4.5 - Validate BST: 
# Implement a function to check if a binary tree is a binary search tree.
#
# A binary search tree (BST) is a binary tree in which every node fits this ordering property: 
#   (all left descendents <= n < all right descendents)
# which must be true for each node n, not just its immediate children.
# 
# Taking this ordering for each individual node is:
#   (Maximum value in left subtree <= current node value < minimum value on right subtree)
# 
# BST could have duplicate values, but this solution assumes no duplicates for simplicity.
#
# This brute force solution will recursively visit all nodes using a Post-Order Traversal (POT)
# Depth-First Search (DFS). It's POT because for each node, it first verifies the left subtree as
# BST, then verifies the right subtree as BST, and finally the tree as is from current node.
# To verify a node as BST, it invokes another DFS to get the maximum left subtree value and minimum
# right subtree tree value. These values are then used to evaluate the above condition.

class Node(object):
    def __init__(self, value):
        self.data = value
        self.children = [None, None]

def is_bst(node):
    if (node == None):
        return 
        
    is_left_subtree_bst = is_bst(node.children[0])
    if ((is_left_subtree_bst is not None) and (not is_left_subtree_bst)):
        return False
    is_right_subtree_bst = is_bst(node.children[1])
    if ((is_right_subtree_bst is not None) and (not is_right_subtree_bst)):
        return False
    print(f"is_left_subtree_bst: {is_left_subtree_bst}, is_right_subtree_bst: {is_right_subtree_bst}")

    left_subtree_max = find_max(node.children[0])
    right_subtree_min = find_min(node.children[1])
    current = node.data
    print(f"current: {current}, left_subtree_max: {left_subtree_max}, right_subtree_min: {right_subtree_min}")

    left_condition = (left_subtree_max is None or left_subtree_max <= current)
    right_condition = (left_subtree_max is None or left_subtree_max <= current)
    print(f"left_condition: {left_condition}, right_condition: {right_condition}")
    is_current_bst = (left_condition and right_condition)
    print(f"is_current_bst: {is_current_bst}")

    return (is_current_bst)

def find_max(node, max_value=None):
    if (node == None):
        return max_value 
    current = node.data
    if (max_value == None or current > max_value):
        max_value = current
    left_max = find_max(node.children[0], max_value)
    right_max = find_max(node.children[1], max_value)
    return max(left_max, right_max)

def find_min(node, min_value=None):
    if (node == None):
        return min_value  
    current = node.data
    if (min_value == None or current < min_value):
        min_value = current
    left_min = find_min(node.children[0], min_value)
    right_min = find_min(node.children[1], min_value)
    return min(left_min, right_min)

# Tests.
def print_tree(node, level=0):
    if node != None:
        print_tree(node.children[1], level + 1)
        print(' ' * 4 * level + '->', node.data)
        print_tree(node.children[0], level + 1)  

root = Node(8)
root.children = [Node(4), Node(10)]
root.children[0].children = [Node(2), Node(6)]
root.children[0].children[0].children = [Node(1), Node(3)]
print_tree(root)
print(f"is_bst (expect True): {is_bst(root)}") 

root = Node(8)
root.children = [Node(4), Node(10)]
root.children[0].children = [Node(6), Node(2)]
root.children[0].children[0].children = [Node(1), Node(3)]
print_tree(root)
print(f"is_bst (expect False): {is_bst(root)}")   