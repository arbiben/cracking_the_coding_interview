# odd = start on the other tower pole
# even = start on the extra pole
import copy

def tower_of_hanoi(num):
    destination =[]
    origin = []
    extra = []
    for i in range(num, 0, -1):
        origin.append(i)

    print_towers(origin, extra, destination)
    move_tower(num, origin, destination, extra)

def move_tower(i, origin, destination, extra):
    if i == 0:
        return 0
    move_tower(i-1, origin, extra, destination)
    move_top(origin, destination)
    print_towers(origin, extra, destination)
    move_tower(i-1, extra, destination, origin)

def move_top(origin, destination):
    destination.append(origin.pop())

def print_towers(aa, bb, cc):
    a = copy.deepcopy(aa)
    b = copy.deepcopy(bb)
    c = copy.deepcopy(cc)

    while a or b or c:
        o = True if (len(a) < len(b) or len(a) < len(c) or len(a)==0) else False
        d = True if (len(c) < len(b) or len(c) < len(a) or len(c)==0) else False
        e = True if (len(b) < len(c) or len(b) < len(a) or len(b)==0) else False

        o = a.pop() if not o else " "
        d = c.pop() if not d else " "
        e = b.pop() if not e else " "

        print("|{}| |{}| |{}|".format(o, e, d))
    print(" O   E   D \n")

tower_of_hanoi(3)
print("Done")
