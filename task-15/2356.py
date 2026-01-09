from itertools import combinations


def f(x):
    P = 10 <= x <= 45
    Q = 35 <= x <= 78
    A = a1 <= x <= a2
    return ((not P) <= Q) and not A


line = [x + eps for x in range(10, 79) for eps in (0, 0.1, 0.9)]
ans = []
for a1, a2 in combinations(line, 2):
    if all(not f(x) for x in line):
        ans += [a2 - a1]
print(min(ans))
