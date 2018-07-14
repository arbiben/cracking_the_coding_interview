# write a method to return all subsets of a set
import copy

def power_set(arr):
    if len(arr) == 0:
        return None
    return get_power_set(arr, [], 0)

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

print(power_set([1,2,3,4]))
