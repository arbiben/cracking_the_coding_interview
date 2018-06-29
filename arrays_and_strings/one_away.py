# given two strings, write a function to check if they are one edit away
# 1. insert a char 2. remove a char 3. swap a char

test_string_one = "pale"
test_string_two = "bake"

def same_len_one_away(w_one, w_two):
    if w_one == w_two:
        return "False"
    
    firstDiff = False

    for i in range(len(w_one)):
        if w_one[i] != w_two[i]:
            if firstDiff:
                return "False"
            
            firstDiff = True

    return "True"

def diff_len_one_away(long_w, short_w):
    firstDiff = False

    for i in range(len(short_w)):
        j = i+1 if firstDiff else i

        if long_w[j] != short_w[i]:
            if firstDiff:
                return "False"
            firstDiff = True
    
    return "True"


def is_one_away(word_one, word_two):
    len_one = len(word_one)
    len_two = len(word_two)

    if abs(len_one - len_two) > 1:
        return "False"

    if len_one == len_two:
        return same_len_one_away(word_one, word_two)

    long_word = word_one if len_one > len_two else word_two
    short_word = word_two if len_one > len_two else word_one

    return diff_len_one_away(long_word, short_word)

print(str(is_one_away(test_string_one, test_string_two)) + " with different defs")
