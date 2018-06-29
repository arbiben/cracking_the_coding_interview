# Implement an algorithm to determine if a string has all unique characters.
# what if you cannot use additional data structures?

test_string = "no duplicates"

def with_data_structure(word):
    letters = set()
    word = "".join(word)

    for letter in word:
        if letter in letters:
            return "False with data structure"
        letters.add(letter)
    
    return "True with data structure"

def without_data_structure(word):
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                return "False without data structure"
    
    return "True without data structure"

print(with_data_structure(test_string))
print(without_data_structure(test_string))
