# 4.4 - Check Balanced: 
# Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.

# This uses Depth-First Search to count the height of both the left and right subtrees from the overall root.

class Node(object):
    def __init__(self, value):
        self.data = value
        self.children = [None, None]

def is_balanced(root):
    left_subtree_height = get_height(root.children[0])
    right_subtree_height = get_height(root.children[1])
    print(f"is_balanced - left_subtree_height: {left_subtree_height} - right_subtree_height: {right_subtree_height}")
    height_difference = abs(left_subtree_height - right_subtree_height)
    return (height_difference <= 1)

def get_height(node, depth=0):
    if (node == None):
        return depth
    depth += 1    
    left_height = get_height(node.children[0], depth)
    right_height = get_height(node.children[1], depth)
    return max(left_height, right_height)

# Tests.
def print_tree(node, level=0):
    if node != None:
        print_tree(node.children[1], level + 1)
        print(' ' * 4 * level + '->', node.data)
        print_tree(node.children[0], level + 1)  

root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4), None]
root.children[0].children[0].children = [Node(6), None]
print_tree(root)
print(f"is_balanced: {is_balanced(root)}")

root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4), None]
print_tree(root)
print(f"is_balanced: {is_balanced(root)}")

root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4), Node(5)]
root.children[1].children = [Node(6), Node(7)]
print_tree(root)
print(f"is_balanced: {is_balanced(root)}")

root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [None, Node(4)]
root.children[0].children[1].children = [None, Node(6)]
print_tree(root)
print(f"is_balanced: {is_balanced(root)}")

root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [None, Node(4)]
print_tree(root)
print(f"is_balanced: {is_balanced(root)}")

root = Node(1)
root.children = [Node(2), Node(3)]
root.children[1].children = [Node(4), None]
root.children[1].children[0].children = [Node(6), None]
print_tree(root)
print(f"is_balanced: {is_balanced(root)}")

root = Node(1)
root.children = [Node(2), Node(3)]
root.children[1].children = [Node(4), None]
print_tree(root)
print(f"is_balanced: {is_balanced(root)}")