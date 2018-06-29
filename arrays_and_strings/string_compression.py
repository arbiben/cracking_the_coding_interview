# implement a method to preform basic compression using counts of repeated characters.
# if the string is the same length, return original string

test_string = "aabcccccaaa"

def compress_string(string):
    compressed_string = ""
    
    i = 0 
    count = 0
    compressed_string = string[0]

    while i < len(string):
        curr_char = string[i]
        if curr_char != compressed_string[-1]:
            compressed_string += str(count)
            curr_char = string[i]
            compressed_string += string[i]
            count = 1
            i+=1
        
        else:
            count += 1
            i+=1
            if i == len(string):
                compressed_string += str(count)

    if len(compressed_string) >= len(string):
        return string

    return compressed_string


print(compress_string(test_string))


