from itertools import combinations


def f(x):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = a1 <= x <= a2
    return C <= ((not A and B) <= (not C))


Oa = sorted([24, 90, 47, 115])
Ox = [x + 0.1 for x in Oa[:-1]]
ans = []
for a1, a2 in combinations(Oa, r=2):
    if all(f(x) for x in Ox):
        ans += [a2 - a1]
print(min(ans))
