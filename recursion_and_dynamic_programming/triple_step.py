# a child is running up a staircase with n steps and can hop either 1,2, or 3 steps
# implement a method to count how many possible ways the child can run up

def triple_step(n):
    if n==0:
        return 0
    return triple_step_helper(n, [1,1,2])

def triple_step_helper(n, l):
    if n<0:
        return 0
    if len(l) > n:
        return l[n]

    next_step = triple_step_helper(n-1, l) + triple_step_helper(n-2, l) + triple_step_helper(n-3, l)
    l.append(next_step)
    return next_step

def triple_bad(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return triple_bad(n-1) + triple_bad(n-2) + triple_bad(n-3)

n = 20
print(triple_step(n))
print(triple_bad(n))
