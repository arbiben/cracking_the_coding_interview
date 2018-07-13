# a magic index in an array is defined to be an index such that a[i] = i
# given a sorted array of distinct integers, write a method to find a magic
# index

def find_magic_index(arr):
    return find_helper(arr, 0, len(arr)-1)

def find_helper(arr, l, r):
    if l>r:
        return -1

    mid = int((l+r)/2)
    if arr[mid] == mid:
        return mid

    if arr[mid] > mid:
        return find_helper(arr, l, mid-1)
    return find_helper(arr, mid+1, r)

arr = [-7,0,1,2,4,7]
bad = [2,3,4,5,6,7]

print("shold return 4: {}".format(find_magic_index(arr)))
print("shold return -1: {}".format(find_magic_index(bad)))
