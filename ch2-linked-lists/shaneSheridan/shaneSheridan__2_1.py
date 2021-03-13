# 2.1 - Remove Dups 
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?
#
# E.g. [1, 2, 3, 2, 4] becomes [1, 2, 3, 4]
# Create a second linked-list and add each unique node to it, so all duplicates are lossed.
#
# Follow up answer: Sort list and then traverse it, removing each "next" duplicate node in turn. 

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

    # Remove node from beginning, when it's the Head, or else from middle or end.
    # For simplicity, if there are two nodes with the given value, just remove the first one.
    def delete(self, value):
        head_node = self.head
        if head_node == None:
            # Head doesn't point to a Node so the list is empty.
            raise ValueError("Cannot delete from empty list.")
        elif head_node.get_data() == value:
            # Remove from beginning.
            self.head = head_node.get_next()
        else:
            # Now, it's known that list is not empty and Head doesn't store value,
            # so must remove either (a) middle, (b) end, or (c) nothing since value doesn't exist in list.
            #
            # Nodes in singly linked lists don't reference their previous Node, only next one,
            # so must use temporary variable (previous) while traversing the list.
            previous = self.head
            current = self.head.get_next()
            while ((current != None) and (current.get_data() != value)):
                # Move to next node.
                current = current.get_next()
                previous = current

            if (current == None):
                raise ValueError("Cannot delete non-existent value from list.")
            else:
                # Remove current node.
                # Changing previous' next to reference current's next node means that current
                # is no longer referenced by any node in the list; effectively removing it.
                previous.set_next(current.get_next())
        self.count -= 1

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

# Create a linked list and insert [1, 2, 3, 2, 4].
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