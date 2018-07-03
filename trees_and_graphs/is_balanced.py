# implement a function to check if a binary tree is balanced 
# two subtrees can't more than 1 level difference

from Node import Node
from create_tree import random_tree # generates trees
import sys

def is_balanced(root):
    if not root:
        return True

    return is_balanced_helper(root) > -1

def is_balanced_helper(root):
    if not root:
        return 0

    left = is_balanced_helper(root.left) + 1
    right = is_balanced_helper(root.right) + 1

    if right == 0 or left == 0 or abs(left-right) > 1:
        return -1

    return max(left, right)

def is_balanced_better(root):
    if not root:
        return -1

    left = is_balanced_better(root.left)
    right = is_balanced_better(root.right)
    if left == -sys.maxsize or right == -sys.maxsize:
        return -sys.maxsize

    diff = abs(left - right)
    if diff > 1:
        return -sys.maxsize

    return max(left, right) + 1

t = random_tree()
balanced = t.balanced
unbalanced = t.unbal

print("Should return True: {}".format(is_balanced(balanced)))
print("Should return False: {}".format(is_balanced(unbalanced)))

print("Better version True: {}".format(-sys.maxsize != is_balanced_better(balanced)))
print("Better version False: {}".format(-sys.maxsize != is_balanced_better(unbalanced)))
