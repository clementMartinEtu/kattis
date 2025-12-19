#https://open.kattis.com/problems/astackofgold?editresubmit=18872536

TUNGSTEN = 29260
DIFF = 110

def solve(w,n):
    total_coins = n * (n + 1) // 2
    base_weight = TUNGSTEN * total_coins
    k = (w - base_weight) // DIFF
    return k

solve(147774000, 100)