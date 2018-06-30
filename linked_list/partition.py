# partition a linked list based on the value p
# any node with the value less than p will appear before
# all the nodes with the value hreater than or equal to p
from LinkedList import Node, LinkedList
import random

def partition(head, p):
    if not head or not head.next:
        return head

    last_less_than = None
    first_gr_eq = None
    new_head = None

    while head:
        temp = head
        head = head.next
        temp.next = None
        if temp.val < p:
            if not new_head:
                new_head = temp
            if not last_less_than:
                last_less_than = temp
            else:
                last_less_than.next = temp
                last_less_than = temp
        else:
            if not first_gr_eq:
                first_gr_eq = temp
            else:
                temp.next = first_gr_eq 
                first_gr_eq = temp
    
    if last_less_than:
        last_less_than.next = first_gr_eq
        return new_head
        
    return first_gr_eq

head = LinkedList.random_linkedlist()
part = random.randint(0,100)
print("partition on {}".format(part))
head.print_linkedlist()
head = partition(head, part)

head.print_linkedlist()
