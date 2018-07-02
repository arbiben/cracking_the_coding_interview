# create a queue from two stacks
from Stack import Stack

class queue_from_stacks:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, val):
        self.s1.push(val)

    def dequeue(self):
        if not self.s2.isEmpty():
            return self.s2.pop()
        else:
            while self.s1.peek():
                self.s2.push(self.s1.pop())

            if not self.s2.isEmpty():
                return self.s2.pop()

        raise ValueError('Queue is empty')

