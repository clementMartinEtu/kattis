#https://open.kattis.com/problems/listgame

def solve(n):

    k = 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            k += 1
        d += 1
    if n > 1:
        k += 1
    return k

solve(127381)