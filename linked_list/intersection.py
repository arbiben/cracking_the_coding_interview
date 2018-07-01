# given two singly linked lists, determine if they intersect or not
from LinkedList import LinkedList
import random

def intersection_with_set(l1, l2):
    set1 = set()
    while l1:
        set1.add(l1)
        l1 = l1.next

    while l2:
        if l2 in set1:
            return l2
        l2 = l2.next
    
    return None

def intersection(l1, l2):
    if not l1 or not l2:
        return None

    len_1 = get_length(l1)
    len_2 = get_length(l2)

    longer = l1 if len_1>len_2 else l2
    short  = l2 if len_1>len_2 else l1

    for _ in range(abs(len_1 - len_2)):
        longer = longer.next

    longer.print_linkedlist()
    short.print_linkedlist()
    while short:
        if short is longer:
            return short

        longer = longer.next
        short = short.next

    return None

def get_length(l):
    count = 0
    while l:
        count += 1
        l = l.next

    return count

# tester
head1 = LinkedList.random_linkedlist(0,100)
head2 = LinkedList.random_linkedlist(0,100)

h1_len = random.randint(1,head1.getSize()-1)
h2_len = random.randint(1,head2.getSize()-1)

inter1 = head1
inter2 = head2
for _ in range(h1_len):
    inter1 = inter1.next

for _ in range(h2_len):
    inter2 = inter2.next

# remove comment here to make two linkedlists intersect
inter1.next = inter2
inter_with_set = intersection_with_set(head1, head2)

inter = intersection(head1, head2)
if inter:
    print("intersection without SET: {}".format(inter.val))
else:
    print("without SET no intersection")

if inter_with_set:
    print("intersection with SET:    {}".format(inter_with_set.val))
else:
    print("with SET no intersection")
