from itertools import combinations


def f(x):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = a1 <= x <= a2
    return not (Q <= ((not A and P) <= (not Q)))


line = [x + eps for x in range(15, 168) for eps in (0, 0.1, 0.9)]
ans = []
for a1, a2 in combinations(line, 2):
    if all(not f(x) for x in line):
        ans += [a2 - a1]
print(min(ans))
