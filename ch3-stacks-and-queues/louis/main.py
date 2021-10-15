class Stack:
    def __init__(self):
        self.head = []
        self.min = None
    def size(self):
        return len(self.head)

    def push(self, item):
        node = self.head
        if self.min is None:
            self.min = item
        else:
            if self.min > item:
                self.min = item
            else:
                self.min = self.min
        if len(node) == 0:
            node.insert(0, item)
        else:

            node.append(item)

    def print(self):
        node = self.head

        print(node)

    def pop(self):
        node = self.head
        if len(node) == 0:
            return []
        v = node.pop(len(node)-1)
        if self.min == v:
            print('ok')
            i = node[0]
            j =1
            while j<len(node):
                if i> node[j]:
                    self.min =node[j]
                else:
                    self.min = i
                j +=1

            return
        else:
            node.pop(len(node) - 1)


    def min(self):
        print(self.min)


class MyQueue:
    def __init__(self):
        self.new = Stack()
        self.old = Stack()
    def size(self):
        return self.old.size() + self.new.size()
    def add(self,v):
        self.new.push(v)
    def shiftStacks(self):
        if self.old.isEmpty():
            while(not self.old.isEmpty()):
                self.old.push(self.new.pop())

    def peek(self):
        self.shiftStacks()
        return self.old.peek()
    def remove(self):
        self.shiftStacks()
        return self.old.pop()





if __name__ == "__main__":
   a = Stack()
   

