class Heap:
    def __init__(self):
        self.l = []

    def pop(self):
        if self.has_next():
            if len(self.l) == 1:
                return self.l.pop()

            r = self.l[0]
            self.l[0] = self.l.pop()
            self.percolate_down()
            return r
        return "Nothing to pop booboo"

    def add(self, data):
        self.l.append(data)
        self.percolate_up()

    def percolate_up(self):
        i = len(self.l)-1
        parent = int(i/2) if i%2==1 else int((i/2)-1)

        while i>0 and self.l[i] < self.l[parent]:
            temp = self.l[i]
            self.l[i] = self.l[parent]
            self.l[parent] = temp
            i = parent
            parent = int(i/2) if i%2==1 else int((i/2)-1)

    def percolate_down(self):
        i = 0
        l = int((i*2) + 1)
        r = int((i*2) + 2)
        n = len(self.l)
        while i<n and l < n and r < n and (self.l[i] > self.l[l] or self.l[i] > self.l[r]):
            percolate_to = l if self.l[l] < self.l[r] else r
            temp = self.l[i]
            self.l[i] = self.l[percolate_to]
            self.l[percolate_to] = temp
            i = percolate_to
            l = int((i*2) + 1)
            r = int((i*2) + 2)

    def has_next(self):
        return len(self.l) > 0

    def print_heap(self):
        print(self.l)

h = Heap()
h.add(7)
h.add(8)
h.add(5)
h.add(10)
h.add(3)
h.add(6)
h.add(9)
h.add(1)
h.print_heap()
while h.has_next():
    print(h.pop())
print(h.pop())
