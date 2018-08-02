# you have a stack of n boxes, with widths w1 heights h1 and depths d1.
# the boxes can be stackes only in a way such that the lower box must be
# larger in w,h and d than the box on top of it. write a fuction that computes
# height of the tallest possible stack. the height of the stack is the sum
# of the heights of each box

import random
def tallestBoxStack(boxes):
    print("Recurse with memoization: {}".format(helperMem(boxes)))
    print("Recurse with and without curr: {}".format(helperSkip(boxes)))

def helperSkip(boxes):
    heightArr = [-1 for _ in range(len(boxes))]
    ans = create_stack_second(boxes, 0, None, heightArr)
    print(heightArr)
    return ans

def create_stack_second(boxes, i, prevBox, heightArr):
    if i >= len(boxes):
        return 0

    curr = boxes[i]
    with_curr = 0
    if canAbove(prevBox, curr):
        with_curr = curr.height + create_stack_second(boxes, i+1, curr, heightArr)

    without_curr = create_stack_second(boxes, i+1, prevBox, heightArr)
    heightArr[i] = max(with_curr, without_curr)
    return heightArr[i]


def helperMem(boxes):
    maxHeight = 0
    heightArr = [-1 for _ in range(len(boxes))]
    for i in range(len(boxes)):
        maxHeight = max(maxHeight, create_stack(boxes, i, heightArr))

    print(heightArr)
    return maxHeight

def create_stack(boxes, i, heightArr):
    if i < len(boxes) and heightArr[i] != -1:
        return heightArr[i]

    curr = boxes[i]
    maxHeight = 0
    for j in range(i+1, len(boxes)):
        if canAbove(curr, boxes[j]):
            maxHeight = max(maxHeight, create_stack(boxes, j, heightArr))
    heightArr[i] = maxHeight = maxHeight + curr.height
    return maxHeight

def canAbove(first, second):
    if first and (second.height >= first.height or second.width >= first.width or second.depth >= first.depth):
        return False
    return True

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
boxes.reverse()
print(boxes)
tallestBoxStack(boxes)
