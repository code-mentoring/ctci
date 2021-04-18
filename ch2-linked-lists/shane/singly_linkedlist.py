class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def get_data(self):
        return self.value

    def set_data(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class SinglyLinkedList(object):

    # 'head' initially stores 'None' until a Node is inserted.
    def __init__(self):
        self.head = None
        self.count = 0

    def get_count(self):
        return self.count

    # For simplicity, only inserts to the beginning of the list.
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1 

    # The last Node is determined by its 'next' reference to 'None' instead of a Node object.
    def find(self, value):
        node = self.head
        while (node != None):
            if node.get_data() == value:
                return node
            else:
                node = node.get_next()
        return None

    def print_data(self):
        is_empty = (self.head == None)
        if (is_empty):
            print("List is empty.")
            return

        output = "[Head:" + str(self.head.get_data())
        current_node = self.head.get_next()
        while (current_node != None):
            #print("Node: ", current_node.get_data())
            output += " -> " + str(current_node.get_data())
            current_node = current_node.get_next()
        output += "]"
        print(output)