# implement a function to check if a binary tree is balanced 
# two subtrees can't more than 1 level difference

from Node import Node
from create_tree import random_tree # generates trees

def is_balanced(head):
    if not head:
        return True

    return is_balanced_helper(head) > -1

def is_balanced_helper(head):
    if not head:
        return 0

    left = is_balanced_helper(head.left) + 1
    right = is_balanced_helper(head.right) + 1

    if right == 0 or left == 0 or abs(left-right) > 1:
        return -1

    return max(left, right)


t = random_tree()
balanced = t.balanced
unbalanced = t.unbal

print("Should return True: {}".format(is_balanced(balanced)))
print("Should return False: {}".format(is_balanced(unbalanced)))