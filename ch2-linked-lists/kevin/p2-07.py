from linkedlist import *

def find_intersect(l1, l2):
    for node in l1:
        match = find_node(l2, node)
        if match:
            return match
    return None

def find_node(ll, target_node):
    for node in ll:
        if node == target_node:
            return node

def main():
    intersection_node = Node(5, Node(6))
    l1 = LinkedList(Node(2, intersection_node))
    l2 = LinkedList(Node(1, intersection_node))
    print("== test case 1 ==")
    print("list 1:", l1)
    print("list 2:", l2)
    print(find_intersect(l1, l2))

    print("== test case 2 ==")
    print("non-intersecting lists.")
    print(find_intersect(make_list(1, 2, 3), make_list(2, 3, 4)))

if __name__ == "__main__":
    main()
