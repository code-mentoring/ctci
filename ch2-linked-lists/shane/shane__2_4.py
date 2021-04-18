# 2.4 Partition: 
# Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values 
# of x only need to be after the elements less than x (see below). The partition element x can 
# appear anywhere in the "right partition"; it does not need to appear between the left and 
# right partitions.
# 
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

def partition(list, x):
    if (list.get_count() <= 1):
        return list

    list_lt_x = SinglyLinkedList()
    list_gre_x = SinglyLinkedList()

    node_cur = list.head
    while (node_cur != None):
        current_data = node_cur.get_data()
        if (current_data < x):
            list_lt_x.insert(current_data)
        else:
            list_gre_x.insert(current_data)    
        node_cur = node_cur.get_next()

    return join_lists(list_lt_x, list_gre_x)      


# Appends list_b onto the end of list_a.
def join_lists(list_a, list_b):
    list_a_end = list_a.head
    while(list_a_end.get_next() != None):
        list_a_end = list_a_end.get_next()

    list_a_end.set_next(list_b.head)
    
    return list_a

# Testing.
from test_helper import *
# [5], x: 5, ans = [5]
aList = get_empty_list()
aList.insert(5)
x = 5
aList.print_data()
partitioned_list = partition(aList, x)
partitioned_list.print_data()

# [5, 3], x: 5, ans = [3, 5]
aList = get_empty_list()
aList.insert(3)
aList.insert(5)
x = 5
aList.print_data()
partitioned_list = partition(aList, x)
partitioned_list.print_data()

# [6, 5, 3], x: 5, ans = [3, 6, 5]
aList = get_empty_list()
aList.insert(3)
aList.insert(5)
aList.insert(6)
x = 5
aList.print_data()
partitioned_list = partition(aList, x)
partitioned_list.print_data()

# [3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1], x: 5, ans = [1 -> 3 -> 3 -> 10 -> 5 -> 8 -> 5]
aList = get_empty_list()
aList.insert(1)
aList.insert(3)
aList.insert(10)
aList.insert(5)
aList.insert(8)
aList.insert(5)
aList.insert(3)
x = 5
aList.print_data()
partitioned_list = partition(aList, x)
partitioned_list.print_data()