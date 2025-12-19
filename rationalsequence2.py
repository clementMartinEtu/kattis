#https://open.kattis.com/problems/rationalsequence2?editresubmit=18872514

def solve(lines):
    results = []

    for k, frac in test_cases:
        p, q = map(int, frac.split('/'))

        bits = []
        while not (p == 1 and q == 1):
            if p > q:
                bits.append('1')
                p -= q
            else:
                bits.append('0')
                q -= p

        binary = '1' + ''.join(reversed(bits))
        n = int(binary, 2)

        results.append((k, n))

    return results


test_cases = [
    (1, "1/1"),
    (2, "1/3"),
    (3, "5/2"),
    (4, "2178309/1346269"),
]

solve(test_cases)