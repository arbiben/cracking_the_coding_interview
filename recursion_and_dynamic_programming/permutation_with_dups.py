# write a method to compute all permutations of a string whose characters
# are not necessarily unique. the list of permutations should not have duplicates

def permutations(s):
    s = list(s)
    s.sort()
    letter_dict = create_dict(s)
    all_permutations = get_permutations(letter_dict, len(s))
    print(all_permutations)
    print(len(all_permutations))

def get_permutations(letter_dict, remaining):
    if remaining == 1:
        return [get_last_letter(letter_dict)]

    all_perms = []
    for key, val in letter_dict.items():
        if val > 0:
            letter_dict[key] -= 1
            perms = get_permutations(letter_dict, remaining - 1)
            for p in perms:
                all_perms.append(key+p)
            letter_dict[key] += 1
    return all_perms

def get_last_letter(dict):
    for key, val in dict.items():
        if val:
            return key

def create_dict(s):
    letter_dict = {}
    for letter in s:
        if letter not in letter_dict:
            letter_dict[letter] = 0
        letter_dict[letter] += 1

    return letter_dict

permutations("aacd")
