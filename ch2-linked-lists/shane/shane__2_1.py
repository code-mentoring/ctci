# 2.1 - Remove Dups 
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?
#
# E.g. [1, 2, 3, 2, 4] becomes [1, 2, 3, 4]
# Create a second linked-list and add each unique node to it, so all duplicates are lossed.
#
# Follow up answer: Sort list and then traverse it, removing each "next" duplicate node in turn. 

from singly_linkedlist import *

def remove_duplicates(list):
    unique_list = SinglyLinkedList()

    current_node = list.head
    while (current_node != None):
        current_value = current_node.get_data()
        is_unique = (unique_list.find(current_value) == None)
        if (is_unique):
                unique_list.insert(current_value)
        current_node = current_node.get_next()

    return unique_list

# Testing.

# Create a linked list and insert [1, 4, 2, 3, 2, 4].
list = SinglyLinkedList()
list.insert(4) # Tail
list.insert(2)
list.insert(3)
list.insert(2)
list.insert(4)
list.insert(1) # Head
list.print_data()
#empty_list = SinglyLinkedList()

result = remove_duplicates(list) 
result.print_data()