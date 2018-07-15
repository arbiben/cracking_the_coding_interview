# write a recursive function to multiply two positive integers without using
# the * operator. others are allowed, but you should minimize the number of operations

def recursive_multiply(a, b):
    smaller = b if a > b else a
    larger = a if a > b else b

    print("recursing and decrementing: {}".format(multiply_decrement(larger, smaller)))
    print("recursion with bit manipulation: {}".format(bit_manipulation(larger, smaller)))
    print("better solution: {}".format(min_product(larger, smaller)))

def multiply_decrement(larger, smaller):
    if smaller == 1:
        return larger

    return multiply_decrement(larger, smaller-1) + larger

def multiply_decrement(larger, smaller):
    if smaller == 1:
        return larger

    return multiply_decrement(larger, smaller-1) + larger

def bit_manipulation(a, b):
    if (a & a-1) == 0 or (b & b-1) == 0:
        return multiply_with_bits(a, b)
    return bit_manipulation(a, b - 1) + a

def multiply_with_bits(a, b):
    perf_power = a if (a & a-1) == 0 else b
    other_num = b if (a & a-1) ==0 else a

    i = 0
    while not perf_power & 1 << i:
        i += 1
    return other_num << i

def min_product(larger, smaller):
    if smaller == 0:
        return 0
    if smaller == 1:
        return larger

    smaller = smaller >> 1
    half = min_product(larger, smaller)

    if half % 2 == 0:
        return half + half
    return half + half + larger

recursive_multiply(7, 33)
