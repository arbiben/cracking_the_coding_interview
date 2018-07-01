# stack that has push pop and getMin

class stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, val):
        if not self.head:
            self.head = Node(val, val)

        else:
            curr_min = self.head.min if self.head.min < val else val
            node = Node(val, curr_min)
            node.next = self.head
            self.head = node

        self.count += 1

    def pop(self):
        if self.count == 0:
            raise ValueError('Stack Underflow Buddy')
        node = self.head
        self.head = self.head.next
        self.count -= 1
        return node

    def peek(self):
        return self.head

    def min(self):
        if self.count == 0:
            raise ValueError('No elements in the stack compadre')
        return self.peek().min

    def isEmpty(self):
        return self.head is None

class Node:
    def __init__(self, val, curr_min):
        self.val = val
        self.min = curr_min
        self.next = None

