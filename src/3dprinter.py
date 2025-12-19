#https://open.kattis.com/problems/3dprinter

def solve(n):
    count  = 1
    nbPrinter = 1
    while nbPrinter < n:
        nbPrinter *= 2
        count += 1

    return count

solve(10)