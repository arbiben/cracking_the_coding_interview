# you have an integer and you can flix exactly one bit
# from 0 to 1. write code to find the length of the longest
# sequence of 1s you could create

def flip_to_win(num):
    if not num:
        return 1
    if num == -1:
        return 204

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

def flip_to_win2(num):
    if num == -1:
        return "WOWNESS"
    sequence = get_sequence(num)
    return find_long_sequence(sequence)

def find_long_sequence(sequence):
    curr_max = 1
    for i in range(0, len(sequence), 2):
        l = 0 if i==0 else sequence[i-1]
        r = 0 if i>=len(sequence)-1 else sequence[i+1]
        if sequence[i] == 1:
            curr_max = max(curr_max, l+1+r)
        elif sequence[i] > 1:
            curr_max = max(curr_max, l+1, r+1)
    return curr_max

def get_sequence(num):
    sequence = []
    comparing_to = 0
    count = 0
    while num:
        if 1 & num != comparing_to:
            sequence.append(count)
            comparing_to = comparing_to ^ 1
            count = 0
        count += 1
        num = num >> 1
    if count:
        sequence.append(count)
    return sequence
    
def flip_to_win3(num):
    if num == -1:
        return "Infinity ya'll"
    curr_max = 1
    prev_count = 0
    count = 0
    while num:
        if num & 1:
            count += 1
        else:
            prev_count = count if num & 2 else 0
            count = 0
        curr_max = max(curr_max, prev_count+1+count)
        num = num >> 1
    return curr_max

# test, example from book
print(flip_to_win(1775))
print(flip_to_win2(1775))
print(flip_to_win3(1775))
