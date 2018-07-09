# you have an integer and you can flix exactly one bit
# from 0 to 1. write code to find the length of the longest
# sequence of 1s you could create

def flip_to_win(num):
    if not num:
        return 1

    shift = 0
    curr_max = 1
    while 1<<shift < num:
        if not 1<<shift & num:
            curr_max = max(curr_max, count_ones(num, shift))
        shift += 1
    return curr_max

def count_ones(num, i):
    l = r = 0
    shift = i + 1
    while 1 << shift & num:
        l += 1
        shift += 1
    shift = i - 1
    while shift > -1 and 1<<shift & num:
        r += 1
        shift -= 1

    return 1 + l + r

# test, example from book
print(flip_to_win(1775))