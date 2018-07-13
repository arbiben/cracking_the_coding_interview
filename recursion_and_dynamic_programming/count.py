
def numDecodings(s):
    if len(s) == 1:
        return 0 if int(s) == 0 else 1
    return count_helper(s, 0)

def count_helper(s, i):
    if i >= len(s):
        return 1
    if i == len(s)-1:
        if s[i] == "0":
            return 0
        return 1

    c = int(s[i])
    c2 = int(s[i+1])
    if c == 0:
        return 0
    if c == 1 or c == 2:
        if c2 == 0 and c == 2:
            return count_helper(s, i+2)
        if c == 1 or (c2>=0 and c2 <= 6):
            return count_helper(s, i+1) + count_helper(s, i+2)

    return count_helper(s, i+1)

print(numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))
