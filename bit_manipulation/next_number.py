# given a positive interger,
# print the next smallest and largest number
# that have the same number of 1's

def next_num(num):
    if not num:
        return None
    first_zero = get_first_zero(num, 0)
    print("Swapping only one bit - not what the question asks")
    print("Number: {} \t\t\tbinary: {}".format(num, "{0:b}".format(num)))
    print_next_largest(num, first_zero)
    print_next_smallest(num, first_zero)
    print_largest(num, first_zero)
    print_smallest(num, first_zero)
    print("\nThis is what the question asks")
    print("Number: {} \t\t\tbinary: {}".format(num, "{0:b}".format(num)))
    print_next_largest_number(num)
    print_next_smallest_number(num)

def print_next_largest_number(num):
    first_one = get_first_non_trailing_one(num)
    ones = count_ones_after_n(num, first_one) - 4
    num = (1 << first_one) ^ num
    
    mask = (1 << first_one) -1
    diff = first_one - ones
    zero_mask = ~((1 << diff) - 1)
    mask = mask & zero_mask
    num = mask | num
    print("next largest: {} \t\tbinary: {}".format(num, "{0:b}".format(num)))

def print_next_smallest_number(num):
    first_zero = get_first_non_trailing_zero(num)
    ones = count_ones_after_n(num, first_zero) - 1
    num = insert_one_and_mask(num, first_zero)
    
    one_mask = ((1 << ones) - 1)
    num = num | one_mask
    print("next smallest: {} \t\tbinary: {}".format(num, "{0:b}".format(num)))

def print_largest(num, first_zero):
    first_one = get_first_one(num)
    largest = swap_bits(num, first_zero, first_one)
    print("largerst swap: {} \t\tbinary: {}".format(largest, "{0:b}".format(largest)))

def print_smallest(num, first_zero):
    last_one = get_last_one(num)
    smallest = swap_bits(num, first_zero, last_one)
    print("smallest swap: {} \t\tbinary: {}".format(smallest, "{0:b}".format(smallest)))

def print_next_largest(num, first_zero):
    if first_zero == 0:
        first_one = get_first_one(num)
        first_zero = get_first_zero(num, first_one)

    next_largest = swap_bits(num, first_zero, first_zero-1)
    print("one larger swap: {} \t\tbinary: {}".format(next_largest, "{0:b}".format(next_largest)))

def print_next_smallest(num, first_zero):
    next_one = get_next_zero(num, first_zero)
    if not next_one:
        print("no num smaller than {}".format(num))
        return
    next_smallest = swap_bits(num, first_zero, next_one)
    print("one swap smaller: {} \tbinary: {}".format(next_smallest, "{0:b}".format(next_smallest)))

def swap_bits(num, zero, one):
    new_num = num | 1 << zero
    new_num = new_num & ~(1<<one)
    return new_num

def get_next_zero(num, first_zero):
    next_zero = first_zero
    while not num & 1<<next_zero:
        if next_zero >= 33:
            return None
        next_zero += 1
    return next_zero

def get_first_zero(num, from_bit):
    first_zero = from_bit
    while num & 1<<first_zero:
        first_zero+=1
    return first_zero

def get_first_one(num):
    first_one = 0
    while not num & 1<<first_one:
        first_one += 1
    return first_one

def get_last_one(num):
    last_one = 32
    while not num & 1<<last_one:
        last_one -= 1
    return last_one

def get_first_non_trailing_zero(num):
    i = 0
    while not 1 << i & num:
        i += 1
    while 1 << i & num:
        i += 1
    return i

def get_first_non_trailing_one(num):
    i = 0
    while not 1 << i & num:
        i += 1
    while 1 << i & num:
        i += 1
    while not 1 << i & num:
        i += 1
    return i

def insert_one_and_mask(num, first_zero):
    num = num | 1 << first_zero
    mask = ~((1 << first_zero) - 1)
    num = mask & num
    return num

def count_ones_after_n(num, n):
    count = 0
    while n > -1:
        if num & 1 << n:
            count += 1
        n -= 1
    return count

next_num(13948)
