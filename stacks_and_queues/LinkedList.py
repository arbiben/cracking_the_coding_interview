# linked list class
# can function as a stack or queue as well
import random
random.seed(a=None, version=2)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def first(self):
        if self.head:
            return self.haed.val
        return None

    def last(self):
        if self.tail:
            return self.tail.val    
        return None

    def first_node(self, val):
        self.head = self.tail = Node(val)
    
    def push(self, val):
        if not self.head:
            self.first_node(val)
        
        else:
            node = Node(val)
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.len += 1

    def pop(self):
        if self.head is None:
            return False

        node = self.head
        selfi.head = self.head.next
        self.head.prev = None
        self.len -=1

        return node.val
    
    def append(self, val):
        if not self.tail:
            self.first_node(val)

        else:
            self.tail.next = Node(val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        
        self.len += 1
    
    def dequeue(self):
        if self.tail is None:
            return False

        node = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.len -=1
        
        return node.val

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

    def isEmpty(self):
        return self.len == 0


    def random_linkedlist(a,b):
        random.seed(a=None, version=2)
        n = random.randint(5, 11)
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
