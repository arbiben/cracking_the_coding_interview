class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.neighbors = set()
        self.touched = False

    def addneighbors(self, *args):
        for node in args:
            self.neighbors.add(node)
