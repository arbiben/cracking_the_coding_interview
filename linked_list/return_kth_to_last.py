# given a singly linked list and k, return the kth element to last
from LinkedList import LinkedList ,Node

def kth_to_last(head, k):
    if head is None or k == 0:
        return None
    
    curr = head
    runner = head
    for _ in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner is not None:
        runner = runner.next
        curr = curr.next

    return curr.val

head = LinkedList.random_linkedlist()
head.print_linkedlist()

print(kth_to_last(head, 5))
