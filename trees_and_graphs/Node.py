class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.neighbors = set()
        self.touched = False

    def addneighbors(self, *args):
        for node in args:
            self.neighbors.add(node)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()
