# Write a function to detemine the number of 
# bits you would need to flip to convert 
# integer A to integer B

def get_bit_flips(a, b):
    shift = 0
    num = 1 << shift
    count = 0 
    while num < a or num < b:
        if num & a ^ num & b:
            count += 1
        shift += 1
        num = 1 << shift
    
    return count

# from book - memorize!
def get_bit_flips2(a,b):
    c = a ^ b
    count = 0
    while c:
        count += c & 1
        c = c >> 1
    return count

# also from book
def get_bit_flips3(a,b):
    c = a ^ b
    count = 0
    while c:
        count += 1
        c = c & (c-1)
    return count

a = 29
b = 15
print("Solution 1, mine: {}".format(get_bit_flips(a, b)))
print("Solution 2, from book: {}".format(get_bit_flips2(a, b)))
print("Solution 3, from book: {}".format(get_bit_flips3(a, b)))