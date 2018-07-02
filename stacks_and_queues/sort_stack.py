# write a program that sorts the elements in a stack using one extra stack
from Stack import Stack

def sort_stack(stack):
    if stack.isEmpty():
        return

    helper = Stack()
    helper.push(stack.pop())

    while stack.hasNext():
        temp = stack.pop()
        if temp > helper.peek():
            helper.push(temp)
        else:
            while helper.hasNext() and temp < helper.peek():
                stack.push(helper.pop())
            
            helper.push(temp)
            
            while stack.hasNext() and helper.peek() <= stack.peek():
                helper.push(stack.pop())


    while helper.hasNext():
        stack.push(helper.pop())

    return stack


s = Stack()

s.push(9)
s.push(0)
s.push(8)
s.push(1)
s.push(7)
s.push(2)
s.push(6)
s.push(3)
s.push(5)
s.push(4)

sort_stack(s)
while s.hasNext():
    print(s.pop())

