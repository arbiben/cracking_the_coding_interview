# given a circular linked list, find the node where the circle begins
from LinkedList import LinkedList, Node
import random

def loop_detection(head):
    fast_runner = head.next.next
    slow_runner = head.next

    while fast_runner is not slow_runner:
        fast_runner = fast_runner.next.next
        slow_runner = slow_runner.next

    while slow_runner is not head:
        slow_runner = slow_runner.next
        head = head.next

    return head

def loop_detection_with_set(head):
    node_list = set()
    
    while head not in node_list:
        node_list.add(head)
        head = head.next

    return head
        
def get_tail(head):
    while head.next:
        head = head.next
    
    return head

# test
head = LinkedList.random_linkedlist(0,100)
intersect_at = random.randint(1, head.getSize()-3)
tail = get_tail(head)
temp = head

head.print_linkedlist()
for _ in range(intersect_at):
    temp = temp.next

tail.next = temp
print("tail is now pointing at {}".format(temp.val))


print("with runners found: {}".format(loop_detection(head).val))
print("with set found: {}".format(loop_detection_with_set(head).val))
