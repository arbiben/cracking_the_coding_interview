# SetOfStacks is composed of several stacks and creates a new stack once 
# the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop()
# behaves identically to a single stack

class SetOfStacks:
    def __init__(self, max_size):
        if max_size < 1:
            raise ValueError('stack size must be at lease 1')
        self.head = None
        self.max = max_size
        self.stackIndex = 0

    def popAt(self, index):
        if index < 0:
            raise ValueError('Index out of bound broski')

        self.head.popAt(index)

    def push(self, val):
        if not self.head:
            self.head = stack(self.max, 0)
            self.stackIndex += 1
        else:
            if self.head.isFull():
                new_stack = stack(self.max, self.head.index + 1)
                new_stack.next = self.head
                self.head = new_stack
                self.stackIndex += 1
            
        self.head.push(val)

    def pop(self):
        if not self.head:
            raise ValueError('Stack Underflow compadre')
        
        node = self.head.pop()

        if self.head.isEmpty():
            self.head = self.head.next
            self.stackIndex -= 1
            self.head 
        
        return node

    def print_stacks(self):
        self.head.print_stacks()


class stack:
    def __init__(self, max_size, index):
        self.head = None
        self.next = None
        self.size = 0
        self.max = max_size
        self.index = index

    def push(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            node = Node(val)
            node.next = self.head
            self.head = node
        
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise ValueError('Stack Underflow my dude')
        
        node = self.head
        self.head = self.head.next
        self.size -= 1

        return node

    def popAt(self, index):
        if index > self.index:
            raise ValueError('Index out of bound mate')

        if index == self.index:
            return self.pop()

        return self.next.popAt(index)

    def isFull(self):
        return self.size == self.max

    def isEmpty(self):
        return self.size == 0

    def print_stacks(self):
        self.head.print_nodes(self.index)
        if self.next:
            self.next.print_stacks()

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_nodes(self, index):
        print(self.val, end=" -> ", flush=True)

        if self.next:
            self.next.print_nodes(index)
        else:
            print("[{}]".format(index))
