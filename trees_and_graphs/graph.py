# generates a graph (not random)
from Node import Node

class gg:
    def __init__(self):
        self.a = Node(0)
        self.b = Node(100)
        self.c = Node(169)
        self.d = Node(45)
        self.e = Node(7)
        self.e = Node(87)
        self.f = Node(45)
        self.g = Node(41)
        self.h = Node(14)
        self.i = Node(4)
        self.j = Node(34)
        self.k = Node(89)
        self.l = Node(21)
        self.m = Node(4)
        self.n = Node(6)
        self.o = Node(9)
        self.p = Node(10)

        self.a.addneighbors(self.g,self.b,self.e)
        self.b.addneighbors(self.a,self.d)
        self.c.addneighbors(self.k,self.d)
        self.d.addneighbors(self.b,self.c,self.i,self.f)
        self.e.addneighbors(self.a,self.l)
        self.f.addneighbors(self.d)
        self.g.addneighbors(self.a,self.h)
        self.h.addneighbors(self.g,self.n)
        self.i.addneighbors(self.d,self.o)
        self.j.addneighbors(self.l)
        self.k.addneighbors(self.c)
        self.l.addneighbors(self.e,self.j)
        self.m.addneighbors(self.p)
        self.n.addneighbors(self.h)
        self.o.addneighbors(self.i)
        self.p.addneighbors(self.m)

    def get(self):
        s = [self.n,self.b,self.i,self.m,self.p]
        return s