# given a string, check if it a permutation of a palindrome

test_string = "ttrsdzreeddffggk"

def convert_to_dict(string):
    letter_dict = {}
    for letter in string:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    return letter_dict

def check_for_palindrome(letter_dict):
    first_odd_number = False

    for key, val in letter_dict.items():
        if val % 2 != 0:
            if first_odd_number:
                return "False"

            first_odd_number = True

    return "True"

def is_palindrome_permutation(string):
    if len(string) == 0 or len(string) == 1:
        return "True"

    string = string.replace(" ","")
    string = string.lower()

    letter_dict = convert_to_dict(string)
    return check_for_palindrome(letter_dict)

def fill_arr(phrase):
    int_val_a = ord('a')

    alphabetic_arr = [0 for _ in range(26)]
    for letter in phrase:
        
        if ord(letter) < 97 or ord(letter) > 122:
            return -1
        
        alphabetic_arr[ord(letter) - int_val_a] += 1
    
    return alphabetic_arr

def check_pal_perm(alphabetic_arr):
    firstOdd = False

    for letter in alphabetic_arr:
        if letter % 2 != 0:
            if firstOdd:
                return "False"
            firstOdd = True
    return "True"

def is_palindrome_perm_arr(phrase):
    phrase = phrase.strip()
    phrase = phrase.replace(" ", "")
    phrase = phrase.lower()

    alphabetic_arr = fill_arr(phrase) 
    if alphabetic_arr == -1:
        return "False"
    
    return check_pal_perm(alphabetic_arr)


print(str(is_palindrome_perm_arr(test_string)) + " with array")
print(str(is_palindrome_permutation(test_string)) + " with dictionary")
