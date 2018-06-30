# given an unsorted linkedlist, remove all duplicates
# assuming it is a singly linked list

from LinkedList import Node

# remove duplicates with a set
def remove_dups_set(head):
    linkedlist = set()
    linkedlist.add(head.val)
    
    while head.next is not None:
        if head.next.val in linkedlist:
            head.next = head.next.next
        else:
            linkedlist.add(head.next.val)
            head = head.next

def remove_dups(head):
    curr = head
    runner = head
    while curr is not None and curr.next is not None:
        while runner.next is not None:
            if runner.next.val == curr.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        
        runner = curr = curr.next


test_head = Node(1)
t = test_head
t.next = Node(1)
t = t.next
t.next = Node(5)
t = t.next
t.next = Node(6)
t = t.next
t.next = Node(2)
t = t.next
t.next = Node(1)
t = t.next
t.next = Node(2)
t = t.next
t.next = Node(9)
t = t.next
t.next = Node(9)
t = test_head

remove_dups(test_head)
while t is not None:
    print(t.val)
    t = t.next


