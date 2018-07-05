# given a list of projects and dependencies determine 
# what is the order of projects to be built. 
# if there is a loop return Error!

from collections import deque
from Node import Node

def build_order(project_list, dependencies):
    if len(project_list) < 2:
        return project_list
    
    projects = {}
    for p in project_list:
        projects[p] = Node(p)
    
    for d in dependencies:
        parent = projects[d[0]]
        child = projects[d[1]]

        parent.children.append(child)
        child.p_count += 1

    queue = deque()
    proj_order = []

    for _, val in projects.items():
        if val.p_count == 0:
            queue.append(val)

    while len(queue) > 0:
        next_proj = queue.popleft()
        proj_order.append(next_proj.val)
        for p in next_proj.children:
            p.p_count -= 1
            if p.p_count == 0:
                queue.append(p)
    
    if len(project_list) != len(proj_order):
        return('Loop detected!')
    else:
        return proj_order


p_list = ['a','b','c','d','e','f']
d_list = [['a','d'],['f','b'],['b','d'],['f','a'],['d','c']]
d_list2 = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c'], ['c','d']]

print("Should return a list: {}".format(build_order(p_list, d_list)))
print("Should an error: {}".format(build_order(p_list, d_list2)))
