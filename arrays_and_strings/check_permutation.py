# Given two strings, write a method to decide if one is a permutation of the other

# base case!!!

string_one = "hello"
string_two = "lloeh"

def create_word_map(string):
    letter_map = {}
    for letter in string:
        if letter in letter_map:
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1

    return letter_map

def check_permutation(letter_map, string):
    
    for letter in string:
        if letter not in letter_map or letter_map[letter] == 0:
            return "False"
        letter_map[letter] -= 1

    return "True"

def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return "False"

    first_word_map = create_word_map(str1.replace(" ",""))
    return check_permutation(first_word_map, str2.replace(" ", ""))

def is_permutation_sort_string(str1, str2):
    if len(str1) != len(str2):
        return "False"
    
    str1 = list(str1)
    str2 = list(str2)

    str1.sort()
    str2.sort()
    
    return str1 == str2

print(str(is_permutation_sort_string(string_one, string_two)) + " with sorted strings")
print(str(is_permutation(string_one, string_two)) + " with map")
