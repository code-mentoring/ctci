#4.2 - Minimal Tree: 
# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create 
# a binary search tree with minimal height.

# A tree is a data structure composed of nodes, with one root node and cannot contain cycles.
# The root has zero or more child nodes, and each child node has zero or more child nodes, and so on
# down to leaf nodes which have no children.
#
# A binary tree is a tree in which each node has up to two children.
#
# A binary search tree is a binary tree in which every node fits the following specific ordering property:
#    (all left descendents <= N < all right descendents)
# This must be true for each node N, and all of its descendents, not just its immediate children.

# This solution uses a recursive algorithm to build the tree, similar to pre-order traversal, with 
# three possible base conditions and returns the Root node. All nodes can be accessed via the Root so
# no overall Tree object is used.

class Node(object):
    def __init__(self, value):
        self.data = value
        self.children = [None, None]

def createMinimalTree(nodes):
    count = len(nodes)
    root = None
    if (count == 1):
        root = Node(nodes[0])
    elif (count == 2):
        root = Node(nodes[0])
        # Array is sorted (asc) so always set right child.
        root.children[1] = Node(nodes[1]) 
    elif (count == 3):
        root = Node(nodes[1])
        root.children = [Node(nodes[0]), Node(nodes[2])] 
    elif (count > 3):
        middle_index = (count//2)
        root = Node(nodes[middle_index])
        left_child = createMinimalTree(nodes[:middle_index])
        right_child = createMinimalTree(nodes[middle_index+1:])
        root.children = [left_child, right_child]

    return root

# Tests.
def printTree(node, level=0):
    if node != None:
        printTree(node.children[0], level + 1)
        print(' ' * 4 * level + '->', node.data)
        printTree(node.children[1], level + 1)

printTree(createMinimalTree([2]))
printTree(createMinimalTree([10, 20]))
print("-------")
printTree(createMinimalTree([2, 4, 6]))
print("-------")
printTree(createMinimalTree([2, 4, 6, 8, 10, 20]))
print("-------")
printTree(createMinimalTree([1,2,3,4,5,6,7,8,9,10]))
print("-------")