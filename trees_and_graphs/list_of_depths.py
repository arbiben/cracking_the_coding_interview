# given a binary tree - create a list of lists where each list contains all the values of a specific depth
from Node import Node

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


# these methods are the same as mininal tree - they were added to create a sample tree
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

# TEST

new_list = [i for i in range(10)]
root = list_to_tree(new_list)
print("DFS: {}".format(list_of_depth(root)))
print("BFS: {}".format(list_of_depth_bfs(root)))
