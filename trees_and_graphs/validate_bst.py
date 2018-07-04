# implement a function to check if 
# a binary tree is a binary search tree

from Node import Node
from create_tree import random_tree
import sys

# this version uses an array 
def validate_bst(root):
    if not root:
        return True

    in_order = []
    validate_bst_helper(root, in_order)

    prev = in_order[0]
    for i in in_order:
        if i < prev:
            return False
        prev = i
    
    return True

def validate_bst_helper(root, in_order):
    if not root:
        return

    validate_bst_helper(root.left, in_order)
    in_order.append(root.val)
    validate_bst_helper(root.right, in_order)

# this method does not use any additional data structure
last = None
def validate_bst_2(root):
    if not root:
        return True
    global last
    
    if not validate_bst_2(root.left):
        return False 

    if last and last >= root.val:
        return False

    last = root.val

    if not validate_bst_2(root.right):
        return False
    
    return True

t = random_tree()
bal = t.balanced
unbal = t.unbal

print("With arr, should print True: {}".format(validate_bst(bal)))
print("No arr, should print True: {}\n".format(validate_bst_2(bal)))

print("With arr, should print False: {}".format(validate_bst(unbal)))
print("No arr, should print False: {}".format(validate_bst_2(unbal)))