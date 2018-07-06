# design an algorithm to count the number of paths
# that sum to a given value

from Node import Node
from create_tree import random_tree
from collections import deque
import copy

# less efficient
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

# Much better solution: RUNNING SUM
def count_paths_running_sum(root, target_value):
    if not root:
        return 0
    return count_running_helper(root, target_value, {}, 0)

def count_running_helper(root, target_value, running_sum, curr):
    if not root:
        return 0

    paths = 0
    curr += root.val
    if curr == target_value:
        paths = 1
    diff = curr - target_value
    if diff in running_sum:
        paths += running_sum[diff]

    if curr in running_sum:
        running_sum[curr] += 1
    else:
        running_sum[curr] = 1
    
    paths += (count_running_helper(root.left, target_value, running_sum, curr)
        + count_running_helper(root.right, target_value, running_sum, curr)) 

    running_sum[curr] -= 1
    curr -= root.val
    return paths


# test    
t = random_tree(15)
tree = t.negative # generates a tree with negative vals

print("Using brute force: {}".format(count_paths(tree, 10)))
print("Using running sum: {}".format(count_paths_running_sum(tree, 10)))
