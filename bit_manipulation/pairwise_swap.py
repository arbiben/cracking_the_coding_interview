# write a program to swap odd and even bits in
# an integer with as few instructions as possible

# my solution
def pairwise_swap(num):
    new_num = 0
    i = 0
    while 1 << i < num:
        first = (1 << i & num) << 1
        second = (1 << (i + 1) & num) >> 1
        new_num = new_num | first | second
        i += 2

    print("{0:b}".format(new_num))

# from book
def pairwise_swap2(num):
    print("{0:b}".format( (num & 0xaaaaaaaaaa) >> 1 | (num & 0x5555555555) << 1 ))

a = 372
pairwise_swap(a)
pairwise_swap2(a)
