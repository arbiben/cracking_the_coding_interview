# given 2 strings check if s2 is a rotation of s1 using one call to 
# x in y (e.g.,"waterbottle"is a rotation of"erbottlewat").

str_1 = "waterbottle"
str_2 = "erbottlewat"

str_3 = "waterbottle"
str_4 = "erbosdfewat"

def is_string_rotation(s1, s2):
    if len(s1) != len(s2) or len(s1)<=1:
        return False

    s1 = str(s1)+str(s1)
    
    return s2 in s1
print("{} and {} should return True:".format(str_1, str_2))
print(is_string_rotation(str_1, str_2))

print("\n{} and {} should return False:".format(str_3, str_4))
print(is_string_rotation(str_3, str_4))
