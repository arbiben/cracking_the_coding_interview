# design an algorithm to count the number of paths
# that sum to a given value

from Node import Node
from create_tree import random_tree
from collections import deque
import copy

def count_paths(root, value):
    if not root:
        return 0

    return count_helper(root, value, deque())

def count_helper(root, value, val_list):
    if not root:
        return 0

    val_list.append(root.val)
    copy_list = copy.deepcopy(val_list)
    count = 0
    if root.val == value:
        count += 1
    while len(copy_list)>1:
        sum_vals = get_sum(copy_list)
        if sum_vals == value:
            count += 1
        copy_list.popleft()

    count += (count_helper(root.left, value, val_list) +
                    count_helper(root.right, value, val_list))
    val_list.pop()
    return count

def get_sum(val_list):
    total = 0
    for v in val_list:
        total += v
    return total

# test
t = random_tree(15)
tree = t.negative # generates a tree with negative vals
print(t.list_of_depth(tree))
print(count_paths(tree, 10))
