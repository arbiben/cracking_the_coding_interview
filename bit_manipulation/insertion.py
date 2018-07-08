# you are given two 32-bit numbers, N and M, and two 
# bit possitions, i and j. write a method to insert M into N
# such that M starts at bit j and ends at bit i

def insertion(n, m, i, j):
    ones = ~0
    left = ones << (j+1)
    right = (ones << i) - 1
    mask = left | right
    masked = n & mask
    m = m << i
    return masked | m

# test from book
print(bin(insertion(1024, 19, 2, 6)))