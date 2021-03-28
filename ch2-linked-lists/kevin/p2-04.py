from linkedlist import *

def partition(ll, x):
    # idea: move nodes with value < x to the start of the list.
    prev = None
    curr = ll.head
    while curr:
        if curr.value < x and prev:
            prev.next_node = curr.next_node
            curr.next_node = ll.head
            ll.head = curr
            # previous node remains the same, just have
            # to update the current node.
            curr = prev.next_node
        else:
            # don't need to move, it's either at the
            # start already or its value is >=x.
            prev = curr
            curr = curr.next_node

def main():
    ll = make_list(5, 6, 1, 2, 3, 2, 4)
    partition(ll, 3)
    print(ll)

if __name__ == "__main__":
    main()
