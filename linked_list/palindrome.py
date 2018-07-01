# check if a linkedlist is a palindrome
from LinkedList import LinkedList, Node
import copy

def is_palindrome(head):
    if not head or not head.next:
        return True

    stack = []
    runner = head

    while runner:
        if not runner.next:
            runner = runner.next
        else:
            runner = runner.next.next
            stack.append(head.val)
        
        head = head.next
    
    while head:
        if len(stack) == 0 or stack.pop() != head.val:
            return False

        head = head.next

    return len(stack) == 0

def is_palindrome_reverse(head):
    if not head or not head.next:
        return True

    rev = reverse_list(copy.deepcopy(head))

    while head:
        if head.val != rev.val:
            return False
        head = head.next
        rev = rev.next

    return True


def reverse_list(l):
    new_list = None
    next_node = l.next

    while l:
        l.next = new_list
        new_list = l
        l = next_node
        next_node = None if not l else l.next
    
    return new_list

head = LinkedList.random_linkedlist(0,1)
head.print_linkedlist()

print("using Iterative approach: {}".format(is_palindrome(head)))

print("using reverse list approach: {}".format(is_palindrome_reverse(head)))
