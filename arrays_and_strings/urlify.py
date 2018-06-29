# write a method to replace all spaces in a string with "%20"

test_string = "that was really hard ya'll"

def urlify(string):
    string = string.strip()
    string = string.split(" ")
    string = "%20".join(string)
    return string

print(urlify(test_string))
