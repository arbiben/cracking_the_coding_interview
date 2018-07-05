# given two nodes, find the first common parent node
# not including the nodes themselves (if seperate trees - return none)
# if a is in a subtree of b - return a.parent

from Node import Node
from create_tree import random_tree

# solution 1
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

# solution 2
def common_parent2(root,a,b):
    if not a or not b:
        return None
    if a is b:
        return a.parent

    if not covers(root, a) or not covers(root, b):
        return None
    if covers(a, b):
        return a.parent
    if covers(b, a):
        return b.parent
    parent = a.parent
    sibling = get_sibling(a)

    while not covers(sibling,b):
        sibling = get_sibling(parent)
        parent = parent.parent
    return parent

def get_sibling(node):
    parent = node.parent
    if node is parent.right:
        return parent.left
    return parent.right

def covers(root, node):
    if not root:
        return False
    if root is node:
        return True
    return covers(root.left, node) or covers(root.right, node)

# solution 3 - assuming there is no link to parent
def common_parent3(root, a, b):
    if not a or not b:
        return None
    if root is a or root is b:
        return root.parent
    if covers(b, a):
        return b.parent
    if covers(a, b):
        return a.parent

    return common_helper(root, a, b)

def common_helper(root, a, b):
    if not root:
        return None
    if root is a or root is b:
        return root
    l = covers2(root.left, a, b)
    r = covers2(root.right, a, b)

    if l and r:
        return root
    if l:
        return common_helper(root.left, a, b)
    return common_helper(root.right, a, b)

def covers2(root, a, b):
    if not root:
        return False
    if root is a or root is b:
        return True
    return covers2(root.left, a, b) or covers2(root.right, a, b)

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
print("First two algorithms have a link to thier parent node")
print("Nodes 8,9 shoud return 7: {}".format(common_parent(nine, eight)))
print("Nodes 4,0 shoud return None: {}".format(common_parent(root, zero)))
print("Nodes 0,2 shoud return 1: {}".format(common_parent(zero, two)))
print("Nodes 0,3 shoud return 1: {}".format(common_parent(zero, three)))
print("Nodes 3,5 shoud return 4: {}\n".format(common_parent(three, five)))

print("Second solution:")
print("Nodes 8,9 shoud return 7: {}".format(common_parent2(root, nine, eight)))
print("Nodes 4,0 shoud return None: {}".format(common_parent2(root, root, zero)))
print("Nodes 0,2 shoud return 1: {}".format(common_parent2(root, zero, two)))
print("Nodes 0,3 shoud return 1: {}".format(common_parent2(root, zero, three)))
print("Nodes 3,5 shoud return 4: {}\n".format(common_parent2(root, three, five)))

print("Third solution, no link to parent:")
print("Nodes 8,9 shoud return 7: {}".format(common_parent3(root, nine, eight)))
print("Nodes 4,0 shoud return None: {}".format(common_parent3(root, root, zero)))
print("Nodes 0,2 shoud return 1: {}".format(common_parent3(root, zero, two)))
print("Nodes 0,3 shoud return 1: {}".format(common_parent3(root, zero, three)))
print("Nodes 3,5 shoud return 4: {}".format(common_parent3(root, three, five)))
