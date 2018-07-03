# given a binary tree - create a list of lists where each list contains all the values of a specific depth
from Node import Node
from create_tree import random_tree

def list_of_depth(root):
    return list_of_depth_helper(root, 0, [])

def list_of_depth_helper(root, d, list_of_lists):
    if not root:
        return None
    
    if len(list_of_lists) == d:
        list_of_lists.append([root.val])
    else:
        list_of_lists[d].append(root.val)

    list_of_depth_helper(root.left, d+1, list_of_lists)
    list_of_depth_helper(root.right, d+1, list_of_lists)

    return list_of_lists

def list_of_depth_bfs(root):
    if not root:
        return None

    final_list = []
    curr = [root]

    while len(curr) > 0:
        final_list.append(curr)
        parents = curr
        curr = []
        for node in parents:
            if node.right:
                curr.append(node.right)
            if node.left:
                curr.append(node.left)
        
    return final_list



# TEST
t = random_tree()
root = t.balanced

print("DFS: {}".format(list_of_depth(root)))
print("BFS: {}".format(list_of_depth_bfs(root)))
