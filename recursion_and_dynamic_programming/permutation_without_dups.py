# write a method to compute all permutations of a string of unique characters

def permutations(s):
    s = list(s)
    permutation_set = get_all_permutations(s)
    print(permutation_set)
    print(len(permutation_set))

def get_all_permutations(s):
    if len(s) == 1:
        return s
    current_perms = []
    for i in range(len(s)):
        letter = s.pop(i)
        all_perms = get_all_permutations(s)
        for perm in all_perms:
            perm += letter
            current_perms.append(perm)
        s.insert(i, letter)
    return current_perms

permutations("abcd")
