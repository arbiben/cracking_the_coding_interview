# a magic index in an array is defined to be an index such that a[i] = i
# given a sorted array of distinct integers, write a method to find a magic
# index

def find_magic_index(arr):
    print("checks without dups: {}".format(find_helper(arr, 0, len(arr)-1)))
    print("checks with dups: {}".format(find_magic_dups(arr, 0, len(arr)-1)))

def find_helper(arr, l, r):
    if l>r:
        return -1

    mid = int((l+r)/2)
    if arr[mid] == mid:
        return mid

    if arr[mid] > mid:
        return find_helper(arr, l, mid-1)
    return find_helper(arr, mid+1, r)

# there are duplicates in the array
def find_magic_dups(arr, l, r):
    if l>r:
        return -1

    mid = int((l+r)/2)

    if arr[mid] == mid:
        return mid

    new_r = min(mid-1, arr[mid])
    right = find_magic_dups(arr, l, new_r)
    if  right > -1:
        return right

    new_l = max(mid+1, arr[mid])
    return find_magic_dups(arr, new_l, r)


arr = [-7,0,1,2,4,7]
bad = [2,3,4,5,6,7]
dups = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]

print("should return 4:")
find_magic_index(arr)
print("\nshould return -1:")
find_magic_index(bad)
print("\nsArray with Dups, should return 2 with dups and 7 without:")
find_magic_index(dups)
