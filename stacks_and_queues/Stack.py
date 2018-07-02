# this is a stack class implementation

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def pop(self):
        if not self.head:
            raise ValueError('Stack underflow my dude')

        node = self.head
        self.head = self.head.next
        self.count -= 1

        return node.val

    def push(self, val):
        if not self.head:
            self.head = Node(val)

        else:
            node = Node(val)
            node.next = self.head
            self.head = node
        
        self.count += 1

    def peek(self):
        return self.head.val
            
    def hasNext(self):
        return not self.isEmpty()

    def isEmpty(self):
        return self.count == 0

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val
