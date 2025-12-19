#https://open.kattis.com/problems/13floors

def solve(n):
    if n < 13:
        return n
    else:
        return n + 1

solve(13)
