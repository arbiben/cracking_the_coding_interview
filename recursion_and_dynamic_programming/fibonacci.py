# fibonacci

def fib(n):
    if n==0 or n==1:
        return 1

    return fib_helper(n, [1,1])

def fib_helper(n, l):
    if len(l) > n:
        return l[n]

    next_num = fib_helper(n-1, l) + fib_helper(n-2, l)
    l.append(next_num)
    return next_num

def fib_iter(n):
    if n==0 or n==1:
        return 1
    a = b = 1
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return b

print(fib(17))
print(fib_iter(17))
