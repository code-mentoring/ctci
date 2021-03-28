from linkedlist import *

def find_loop(ll):
    # I can't think of a way to find the FIRST node
    # in the loop without tracking all of the nodes
    # that have been seen so far.
    nodes = []
    for node in ll:
        # this relies on Node not having an __eq__ implementation,
        # it should compare by reference.
        if node in nodes:
            return node
        nodes.append(node)
    return None

def main():
    print("== test case 1 ==")
    print("non-looping list")
    print(find_loop(make_list(1, 2, 3)))

    print("== test case 2 ==")
    print("single node that loops back to itself")
    node = Node(5)
    node.next_node = node
    print(find_loop(LinkedList(node)))

    print("== test case 3 ==")
    print("a good ol' loop")
    last = Node(5)
    first = Node(3, Node(4, last))
    last.next_node = first
    print(find_loop(LinkedList(Node(1, Node(2, first)))))

if __name__ == "__main__":
    main()
