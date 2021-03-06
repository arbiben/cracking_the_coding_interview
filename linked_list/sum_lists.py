# given two linked lists where every node is a digit
# return one linked list with the sum of both linkedlist

from LinkedList import Node, LinkedList

# first digit (most left) is the actually the most right 
def sum_lists(l1, l2):
    borrow = 0
    head = None
    tail = None
    
    while l1 or l2:
        sum_lists = borrow + (0 if not l1 else l1.val)
        sum_lists += 0 if not l2 else l2.val

        if sum_lists > 9:
            borrow = 1
            sum_lists -= 10
        else:
            borrow = 0

        new_node = Node(sum_lists)
        if not head:
            head = new_node
        else:
            tail.next = new_node
        tail = new_node

        l1 = None if not l1 else l1.next
        l2 = None if not l2 else l2.next

    if borrow:
        tail.next = Node(borrow)
        tail = tail.next
    
    return head

def sum_lists_recursive(l1, l2):
    return sum_list_helper(l1, l2, 0)

def sum_list_helper(l1, l2, borrow):
    if not l1 and not l2 and borrow == 0:
        return None

    sum_elems = borrow + (0 if not l1 else l1.val)
    sum_elems += 0 if not l2 else l2.val
    
    if sum_elems > 9:
        borrow = 1
        sum_elems -=10
    else:
        borrow = 0

    l1 = None if not l1 else l1.next
    l2 = None if not l2 else l2.next

    node = Node(sum_elems)
    node.next = sum_list_helper(l1, l2, borrow) 

    return node

def reverse_list(l):
    new_list = None
    next_node = l.next

    while l:
        l.next = new_list
        new_list = l
        l = next_node
        next_node = None if not l else l.next
    
    return new_list


first = LinkedList.random_linkedlist()
second = LinkedList.random_linkedlist()
first.print_linkedlist()
second.print_linkedlist()

print("iterative")
sum_lists(first, second).print_linkedlist()

print("revcursive")
sum_lists_recursive(first, second).print_linkedlist()
# for the FOLLOW UP - just run the lists in the reverse list funcion
