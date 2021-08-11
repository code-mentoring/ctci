class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next


    def remove_dups(self):
        prev = self.head
        node = prev.next

        values = []
        while node is not None:
            if node.item in values:
                prev.next = prev.next.next

            values.append(node.item)
            node = node.next
            prev = prev.next

    def return_kthToLast(self, n):
        node = self.head
        counter = 0
        second_counter = 0
        while node is not None:
            counter += 1
            node = node.next
        result = counter - n
        node = self.head
        while node is not None:
            second_counter += 1
            if second_counter == result:
                val = node.item
                return val
            else:

                node = node.next
    def delete_middleNode(self):
        node = self.head
        c = 0
        v = 0

        while node is not None:
            c += 1
            v = 0
            node = node.next
        c = c // 2
        prev = self.head
        node = prev.next
        while prev is not None:
            v += 1
            if v == c - 1:
                prev.next = prev.next.next
            else:
                node = node.next
                prev = prev.next





if __name__ == "__main__":
   a = Linked_List()
   a.append(1)
   a.append(2)
   a.append(0)
   a.append(2)
   a.append(1)
