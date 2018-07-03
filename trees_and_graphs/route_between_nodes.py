# given two nodes, determine if there is a route between them

from graph import gg
from Node import Node
from collections import deque

def is_route(a, b):
    if not a or not b:
        return False

    if a is b:
        return True

    queue = deque()
    touched = set()

    queue.append(a)
    touched.add(a)

    while len(queue) > 0:
        n = queue.popleft()
        if n is b:
            return True

        for node in n.neighbors:
            if node not in touched:
                queue.append(node)
                touched.add(node)

    return False

def is_route_dfs(a, b):
    if not a or not b:
        return False

    return is_rout_helper(a, b, set())

def is_rout_helper(curr, destination, touched):
    if curr is destination:
        return True

    touched.add(curr)
    
    for node in curr.neighbors:
        if node not in touched and is_rout_helper(node, destination, touched):
            return True

    return False

g = gg().get()
print("BFS: {}".format(is_route(g[0],g[2])))
print("DFS: {}".format(is_route_dfs(g[0], g[2])))
