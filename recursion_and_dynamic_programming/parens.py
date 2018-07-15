# implement an algorithm to print all valid combinations of n pairs of parentheses
# input: 3 output: ((())) ()(()) (())() ()()() (()())

def parens(n):
    if n == 0:
        return None
    if n == 1:
        return ["()"]

    prev_parens = parens(n-1)
    new_parens = set()
    for p in prev_parens:
        for i in range(len(p)):
            if p[i] == '(':
                temp = p[:i+1] + "()" + p[i+1:]
                new_parens.add(temp)
        new_parens.add("()"+p)
    return new_parens
    
print(parens(3))
