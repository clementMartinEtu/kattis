#https://open.kattis.com/problems/lvable

def solve(n, s):
    if "lv" in s:
        return 0
    elif "vl" in s:
        return 0
    elif 'l' in s and 'v' in s:
        return 1
    elif 'l' in s or 'v' in s:
        return 1
    else:
        return 2

solve(7, "lovable")