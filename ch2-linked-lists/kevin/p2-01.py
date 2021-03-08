from linkedlist import *

def remove_dups(ll):
    # No temporary buffer.
    curr = ll.head
    while curr:
        n = curr
        while n:
            if n.next_node and n.next_node.value == curr.value:
                # The next node is a duplicate, so
                # make the pointer point at the node
                # AFTER the next one, effectively
                # removing it from the list.
                n.next_node = n.next_node.next_node
            else:
                n = n.next_node
        curr = curr.next_node

def main():
    cases = [
        (make_list(1, 2, 3, 1, 1, 3, 4),
         make_list(1, 2, 3, 4)),
        (make_list(1, 1), make_list(1)),
        (make_list(), make_list())
    ]
    for (ll, expected) in cases:
        remove_dups(ll)
        print(expected == ll, expected, ll)

if __name__ == "__main__":
    main()
