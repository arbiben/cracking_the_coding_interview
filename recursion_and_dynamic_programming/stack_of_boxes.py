# you have a stack of n boxes, with widths w1 heights h1 and depths d1.
# the boxes can be stackes only in a way such that the lower box must be
# larger in w,h and d than the box on top of it. write a fuction that computes
# height of the tallest possible stack. the height of the stack is the sum
# of the heights of each box
import random

class Box:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def __str__(self):
        return "\nheight: {}, width: {}, depth: {}".format(self.height, self.width, self.depth)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if self.height == other.height:
            if self.width == other.width:
                return self.depth < other.depth
            return self.width < other.width
        return self.height < other.height

    def __gt__(self, other):
        return other.__lt__(self)

    def __eq__(self, other):
        return self.height == other.height

    def __ne__(self,other):
        return not self.__eq__(other)

def create_list_of_boxes(n):
    boxes = []
    a = 1
    b = 20
    for _ in range(n):
        h = random.randint(a, b)
        w = random.randint(a, b)
        d = random.randint(a, b)

        boxes.append(Box(h,w,d))
    return boxes

# test
boxes = sorted(create_list_of_boxes(10))
print(boxes)
#print("regular recursion: {}".format(tallestBoxStack(boxes)))
print("memoization: {}".format(tallestBoxStackMem(boxes)))
