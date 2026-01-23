from itertools import combinations


def f(x):
    B = 54 <= x <= 120
    C = 78 <= x <= 151
    A = a1 <= x <= a2
    return C <= ((B and not A) <= (not C))


Oa = sorted([54, 120, 78, 151])
Ox = [x + 0.5 for x in Oa[:-1]]
ans = []
for a1, a2 in combinations(Oa, 2):
    if all(f(x) for x in Ox):
        ans += [a2 - a1]
print(min(ans))
