# Node data structure for all the questions in this chapter

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.neighbors = set()
        self.children = []
        self.p_count = 0
        self.status = None

    def addneighbors(self, *args):
        for node in args:
            self.neighbors.add(node)

    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        return self.__str__()

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()
