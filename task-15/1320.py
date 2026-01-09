from itertools import combinations


def f(x):
    P = 10 <= x <= 25
    Q = 15 <= x <= 30
    R = 25 <= x <= 40
    A = a1 <= x <= a2
    return (Q <= (not R)) and A and not P


line = [x + eps for x in range(10, 40 + 1) for eps in (0, 0.1, 0.9)]
ans = []
for a1, a2 in combinations(line, 2):
    if all(not f(x) for x in line):
        ans += [a2 - a1]
print(max(ans))
