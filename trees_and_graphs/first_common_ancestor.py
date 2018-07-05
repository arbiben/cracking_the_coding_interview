# given two nodes, find the first common parent node
# not including the nodes themselves (if seperate trees - return none)
from Node import Node
from create_tree import random_tree

def common_parent(a,b):
    if not a or not b:
        return None
    if a is b:
        return a.parent

    len_a = get_len(a)
    len_b = get_len(b)
    longer = a if len_a > len_b else b
    shorter = b if len_a > len_b else a
    diff = abs(len_a-len_b)

    for _ in range(diff):
        longer = longer.parent

    if longer is shorter:
        return longer.parent
    
    while longer and shorter:
        if longer is shorter:
            return longer
        longer = longer.parent
        shorter = shorter.parent
    
    return None

def get_len(node):
    if not node:
        return 0
    count = 0
    while node:
        count += 1
        node = node.parent
    return count

# test
t = random_tree()
root = t.balanced
seven = root.right
five = seven.left
eight = seven.right
nine = eight.right
six = five.right
one = root.left
zero = one.left
two = one.right
three = two.right

print("Nodes 8,9 shoud return 7: {}".format(common_parent(nine, eight)))
print("Nodes 4,0 shoud return None: {}".format(common_parent(root, zero)))
print("Nodes 0,2 shoud return 1: {}".format(common_parent(zero, two)))
print("Nodes 0,3 shoud return 1: {}".format(common_parent(zero, three)))
print("Nodes 3,5 shoud return 4: {}".format(common_parent(three, five)))
