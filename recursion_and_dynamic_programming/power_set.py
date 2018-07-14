# write a method to return all subsets of a set
import copy

def power_set(arr):
    if len(arr) == 0:
        return None
    one = get_power_set(arr, [], 0)
    one.sort()
    two = get_power_set_binary(arr)
    two.sort()
    print("my way: {}".format(one))
    print("binary: {}".format(two))

def get_power_set(arr, subsets, i):
    if i == len(arr):
        subsets.append([])
        return subsets

    arr_copy = copy.deepcopy(subsets)
    element = arr[i]
    for set in arr_copy:
        set.append(element)
    subsets.append([element])
    subsets.extend(arr_copy)
    return get_power_set(arr, subsets, i+1)

def get_power_set_binary(arr):
    subsets = []
    size = 1 << len(arr) # size of the subsets list
    for i in range(size):
        set = create_subset(arr, i)
        subsets.append(set)
    return subsets

def create_subset(arr, i):
    index = 0
    set = []
    while i:
        if i & 1:
            set.append(arr[index])
        i = i >> 1
        index += 1
    return set

power_set([1,2,3,4])
