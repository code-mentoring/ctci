# 2.2 Return Kth to Last 
# Implement an algorithm to find the kth to last element of a singly linked list.

# Solution uses length of list to calculate index of Kth to last node,
# (length - k) = i
# E.g. for list: [1, 2, 3] and k: 3,
#      3rd last node is 1 with index 0,
#      so i = (length - k) = (3 - 3) = 0
#      
# Then traverse to node with index i and return its value.

def get_k_last(k, list):
    list_length = list.get_count()
    is_k_valid = ((k < 1) or (k > list.get_count()))
    if (is_k_valid):
        raise ValueError(f"Invalid k value {k} for list length {list_length}; must be '0 < k <= length'.")
    elif (list_length == 1):
        return list.head.get_data()
    else:
        i = list_length - k
        current_i = 0
        current_node = list.head
        while (current_i != i):
            current_node = current_node.get_next()
            current_i += 1
        return current_node.get_data()


# Testing.
from singly_linkedlist import *

def get_empty_list():
    return SinglyLinkedList()

def evaluate(expect, actual):
    print({True: "Pass.", False: "FAIL!!!"} [expect==actual] +" -- "+ f"Expect {expect}, actual {actual}.")

# [1], k = 1, ans = 1
aList = get_empty_list()
aList.insert(1)
k = 1
expect = 1
actual = get_k_last(k, aList)
evaluate(expect, actual)
# [1], k = 2, ans = error
k = 2
try:
    actual = get_k_last(k, aList)
    print("FAIL!!! -- Expect ValueError.")
except ValueError as ve:
    print("Pass -- Expect ValueError.")
    print(ve)
# [1, 2, 3], k = 1, ans = 3
aList = get_empty_list()
aList.insert(3)
aList.insert(2)
aList.insert(1)
k = 1
expect = 3
actual = get_k_last(k, aList)
evaluate(expect, actual)
# [1, 2, 3], k = 1, ans = 2
k = 2
expect = 2
actual = get_k_last(k, aList)
evaluate(expect, actual)
# [1, 2, 3], k = 3, ans = 1
k = 3
expect = 1
actual = get_k_last(k, aList)
evaluate(expect, actual)
# [1, 2, -3, "hello", 5], k = 2, ans = "hello"
aList = get_empty_list()
aList.insert(5)
aList.insert("hello")
aList.insert(-3)
aList.insert(2)
aList.insert(1)
k = 2
expect = "hello"
actual = get_k_last(k, aList)
evaluate(expect, actual)