# implementation of a list that holds three stacks
# this is the static version (not the most efficient)

class three_stacks:
    def __init__(self, list_size):
        self.stacks = 3
        self.last_elem = list_size
        self.list = [0 for _ in range(list_size)]
        self.pointer = {}
        self.size = {}
        self.max_size = int(list_size / 3)
        for i in range(3):
            self.pointer[i] = int((list_size/3)*i)
        for i in range(3):
            self.size[i] = 0


    def push(self, stack_num, elem):
        if stack_num == 2 and self.pointer[2] == self.last_elem:
            raise ValueError('Stack overflow')
        elif self.size[stack_num] == self.max_size:
            raise ValueError('Stack overflow')

        print(self.size[stack_num])
        self.list.insert(self.pointer[stack_num], elem)
        self.pointer[stack_num] += 1
        self.size[stack_num] += 1
        return True
        
    def pop(self, stack_num):
        if self.size[stack_num] == 0:
            raise ValueError('Stack underflow')

        self.pointer[stack_num] -= 1
        self.size[stack_num] -= 1
        return self.list[self.pointer[stack_num]]
    
    def isEmpty(self, stack_num):
        return self.size[stack_num] == 0
