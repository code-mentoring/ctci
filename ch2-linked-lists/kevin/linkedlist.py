class LinkedList:
    def __init__(self, head):
        self.head = head

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return False
        self_ptr = self.head
        other_ptr = other.head
        while self_ptr and other_ptr:
            if self_ptr.value != other_ptr.value:
                return False
            self_ptr = self_ptr.next_node
            other_ptr = other_ptr.next_node
        return self_ptr is None and other_ptr is None

    def __str__(self):
        values = []
        curr = self.head
        while curr:
            values.append(curr.value)
            curr = curr.next_node
        return ("LinkedList("
                + "->".join(map(str, values))
                + ")")

    def __repr__(self):
        return str(self)

    def __iter__(self):
        curr = self.head
        def gen():
            nonlocal curr
            while curr:
                result = curr
                curr = curr.next_node
                yield result
        return gen()

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return "Node(" + str(self.value) + ", " + ("has next" if self.next_node else "no next")+ ")"

    def __repr__(self):
        return str(self)

def make_list(*values):
    head = None
    current = None
    for value in values:
        next_node = Node(value)
        if current:
            current.next_node = next_node
            current = next_node
        else:
            current = next_node
            head = next_node
    return LinkedList(head)
