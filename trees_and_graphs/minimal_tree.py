# given a sorted list - transform it to a BST

from Node import Node

def list_to_tree(l):
    return to_tree_helper(l, 0, len(l)-1)

def to_tree_helper(sorted_list, l, r):
    if l > r:
        return None 
    mid = int((l+r)/2)
    node = Node(sorted_list[mid])
    node.left = to_tree_helper(sorted_list, l, mid-1)
    node.right = to_tree_helper(sorted_list, mid+1, r)

    return node

new_list = [i for i in range(10)]
root = list_to_tree(new_list)