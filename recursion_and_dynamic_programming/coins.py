# given an infinite number of quarters, dimes, nickels, and pennies -
# write code to calculate the number of ways or representing n cents

def coins(n):
    return count_quarters(n)

def count_quarters(n):
    if n <= 0:
        return 0
    q = 0
    ans = 0
    while n > q:
        ans += count_dimes(n-q)
        q += 25
    return ans

def count_dimes(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    d = 0
    ans = 0
    while n > d:
        ans += count_nickels(n-d)
        d += 10
    return ans

def count_nickels(n):
    if n == 0:
        return 1
    n_amnt = 0
    ans = 0
    while n > n_amnt:
        ans += 1
        n_amnt += 5
    return ans

print(coins(26))
