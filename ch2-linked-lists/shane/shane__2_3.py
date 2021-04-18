# 2.3 Delete Middle Node. 
# Implement an algorithm to delete a node in the middle (i.e., any node but 
# the first and last node, not necessarily the exact middle) of a singly linked list, 
# given only access to that node.
#
# E.g. 
# Input: the node c from the linked list a -> b -> c -> d -> e -> f 
# Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f

def remove_from_middle_only(list, data_to_remove):
    current = list.head        
    while (current.get_next() != None): 
        next = current.get_next() 
        if ((next.get_data() == data_to_remove) and 
            (next.get_next() != None)): # Ignore last node.
            delete_next_node(current)
        current = current.get_next()

def delete_next_node(node):
    new_next = node.get_next().get_next()
    node.set_next(new_next)

# Testing.
from test_helper import *
# [a], remove: a, ans = [a]
aList = get_empty_list()
aList.insert('a')
data_to_remove = 'a'
aList.print_data()
remove_from_middle_only(aList, data_to_remove)
aList.print_data()

# [a, b], remove: a, ans = [a, b]
aList = get_empty_list()
aList.insert('b')
aList.insert('a')
data_to_remove = 'a'
aList.print_data()
remove_from_middle_only(aList, data_to_remove)
aList.print_data()

# [a, b], remove: b, ans = [a, b]
aList = get_empty_list()
aList.insert('b')
aList.insert('a')
data_to_remove = 'b'
aList.print_data()
remove_from_middle_only(aList, data_to_remove)
aList.print_data()

# [a, b, c], remove: b, ans = [a, c]
aList = get_empty_list()
aList.insert('c')
aList.insert('b')
aList.insert('a')
data_to_remove = 'b'
aList.print_data()
remove_from_middle_only(aList, data_to_remove)
aList.print_data()

# [a, b, c, d], remove: b, ans = [a, c, d]
aList = get_empty_list()
aList.insert('d')
aList.insert('c')
aList.insert('b')
aList.insert('a')
data_to_remove = 'b'
aList.print_data()
remove_from_middle_only(aList, data_to_remove)
aList.print_data()

# [a, b, c, d], remove: b, ans = [a, b, c, d]
aList = get_empty_list()
aList.insert('d')
aList.insert('c')
aList.insert('b')
aList.insert('a')
data_to_remove = 'd'
aList.print_data()
remove_from_middle_only(aList, data_to_remove)
aList.print_data()

# [a, b, c, d], remove: b, ans = [a, b, c, d]
aList = get_empty_list()
aList.insert('d')
aList.insert('c')
aList.insert('b')
aList.insert('a')
data_to_remove = 'a'
aList.print_data()
remove_from_middle_only(aList, data_to_remove)
aList.print_data()