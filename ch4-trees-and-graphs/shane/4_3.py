# 4.3 - List of Depths: 
# Given a binary tree, design an algorithm which creates a linked list of all the nodes 
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
#
# Depth-First Search (DFS) starts at one node (e.g. root) and visits each branch completely before moving
# on to the next branch, i.e. go deep first before going wide, until all nodes have been visited.
#
# This solution uses a Pre-Order Traversal form of DFS to build a dictionary (i.e. Key->Value pairs)
# to store each depth as integer keys and a list of nodes at each depth as values.
# No need to check if nodes have been visited during DFS because trees cannot have cycles. 

class Node(object):
    def __init__(self, value):
        self.data = value
        self.children = [None, None]

def create_lists_of_depths(node, depth=0, lists={}):
    if (node == None):
        return

    add_to_lists(node, depth, lists) 
    create_lists_of_depths(node.children[0], depth+1, lists)
    create_lists_of_depths(node.children[1], depth+1, lists)

    return lists

def add_to_lists(node, depth, lists):
    list = lists.get(depth)
    if (list == None):
        list = []
        lists[depth] = list
    list.append(node)    

# Tests.
def print_tree(node, level=0):
    if node != None:
        print_tree(node.children[0], level + 1)
        print(' ' * 4 * level + '->', node.data)
        print_tree(node.children[1], level + 1)

def print_lists(lists):
    print(f"Printing lists...")
    for depth, list in lists.items():
       print(f"Depth: {depth}, List: {list_to_string(list)}")

def list_to_string(list):
    str = ""
    for n in list:
        str += f"-> {n.data}"
    return str    

root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4), Node(5)]
root.children[1].children = [Node(6), Node(7)]
print_tree(root)

print_lists(create_lists_of_depths(root))

# Todo: Below code works but old data needs to be cleared somehow.
#root = Node(1)
#root.children = [Node(2), Node(3)]
#print_tree(root)
#print_lists(create_lists_of_depths(root))