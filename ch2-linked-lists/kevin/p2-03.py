from linkedlist import *

def delete_node(ll, node):
    curr = ll.head
    while curr:
        if curr.next_node == node:
            curr.next_node = curr.next_node.next_node
            break
        curr = curr.next_node

def main():
    ll = make_list(1, 2, 3, 4)
    node = ll.head.next_node.next_node # should be 3
    delete_node(ll, node)
    print(ll == make_list(1, 2, 4))

if __name__ == "__main__":
    main()
