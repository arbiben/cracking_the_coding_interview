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


g = gg().get()
print(is_route(g[0],g[3]))