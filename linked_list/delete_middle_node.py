# given a node in a link list, delete it.
# this node cannot be the first or last node.
from LinkedList import Node, LinkedList
import random
def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next


# tester - generate a linkedlist greater that 3 and check the algorithm

size = 0
n = 0
while size<3:
    head = LinkedList.random_linkedlist()
    size = head.getSize()
    n = random.randint(1,size-2)

head.print_linkedlist()
print("delete at location {}".format(n))

node = head
for _ in range(n):
    node = node.next

delete_node(node)

head.print_linkedlist()
