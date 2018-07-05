# create an algorithm that determines if t2 is a subtree of t1

from Node import Node
from create_tree import random_tree

def check_subtree(t1, t2):
    if not t2:
        return True

    if not t1:
        return False

    return check_subtree_helper(t1, t2)

def check_subtree_helper(t1,t2):
    if not t2:
        return False
    if t1.val == t2.val:
        if is_sub(t1, t2):
            return True

    if check_subtree_helper(t1, t2.right) or check_subtree_helper(t1, t2.left):
        return True
    return False

def is_sub(t1,t2):
    if not (t1 or t2):
        return True

    if t1.val != t2.val:
        return False

    if is_sub(t1.left, t2.left) and is_sub(t1.right, t2.right):
        return True

    return False

def check_subtree2(t1, t2):
    if not t2:
        return True
    if not t1:
        return False

    t1_pre_order = get_pre_order(t1, [])
    t2_pre_order = get_pre_order(t2, [])

    t2_pre_order = (','.join(str(x) for x in t2_pre_order))
    t1_pre_order = (','.join(str(x) for x in t1_pre_order))
    if t1_pre_order in t2_pre_order:
        return True
    return False

def get_pre_order(root, l):
    if not root:
        l.append('X')
        return

    l.append(root.val)
    get_pre_order(root.left, l)
    get_pre_order(root.right, l)

    return l

t = random_tree(15)
tree = t.balanced

other = Node(13)
other.right = Node(14)
other.left = Node(12)
left = Node(9)
left.left = Node(8)
left.right = Node(10)
root = Node(11)
root.right = other
root.left = left

print("Should return True: {}".format(check_subtree2(root, tree)))
print("Should return False: {}".format(check_subtree2(tree, root)))

