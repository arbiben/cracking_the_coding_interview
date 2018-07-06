# given a BST (all unique numbers), print all possible arrays 
# that could have led to this tree

### THE OUTPUT IS NOT CORRECT

from Node import Node
from create_tree import random_tree
from collections import deque
import copy

def all_sequences(root):
    result = []
    if not root:
        result.append([])
        return result

    prefix = []
    prefix.append(root.val)
    left = all_sequences(root.left)
    right = all_sequences(root.right)

    for l in left:
        for r in right:
            weaved = []
            weave_lists(l, r, weaved, prefix)
            result.append(weaved)

    return result

def weave_lists(left, right, result, prefix):
    if len(left) == 0 or len(right) == 0:
        prev_results = copy.deepcopy(prefix)
        prev_results.append(left)
        prev_results.append(right)
        result.append(prev_results)
        return
    
    save = left.pop(0)
    prefix.append(save)
    weave_lists(left, right, result, prefix)
    prefix.pop()
    left.insert(0, save)

    save = right.pop(0)
    prefix.append(save)
    weave_lists(left,right, result, prefix)
    prefix.pop()
    right.insert(0, save)

t = random_tree(6)
root = t.balanced
ans = all_sequences(root)
