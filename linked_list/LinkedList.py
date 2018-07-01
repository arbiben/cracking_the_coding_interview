# linked list class
# can function as a stack or queue as well
import random
random.seed(a=None, version=2)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def push(self, val):
        new_node = Node(val)
        if self.len == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.len += 1

    def pop(self):
        if self.head is None:
            return False

        self.head = self.head.next
        self.head.prev = None
        self.len -=1
        return True
    
    def append(self, val):
        new_node = Node(val)
        if self.len == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.len += 1
    
    def dequeue(self):
        if self.tail is None:
            return False

        self.tail = self.tail.prev
        self.tail.next = None
        self.len -=1
        return True

    def remove(self, node):
        if node is None:
            return False

        if node is self.head:
            pop()
        elif node is self.tail:
            dequeue()
        
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

        self.len -= 1
        
        return True

    def random_linkedlist(a,b):
        random.seed(a=None, version=2)
        n = random.randint(1, 10)
        head = Node(random.randint(a,b))
        t = head
        for _ in range(n):
            t.next = Node(random.randint(a,b))
            t = t.next

        return head

# a Node for a linked list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def getSize(self):
        if self.next is None:
            return 1
        return self.next.getSize()+ 1

    def print_linkedlist(self):
        print(self.val, end=" -> ", flush=True)

        if self.next is not None:
            self.next.print_linkedlist()
        else:
            print("None")
