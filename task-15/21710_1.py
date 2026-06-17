from itertools import combinations


def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = a1 <= x <= a2
    return (not A) <= (B == C)


Oa = sorted([36, 75, 60, 110])
Ox = [x + 0.1 for x in Oa[:-1]]
ans = []
for a1, a2 in combinations(Oa, r=2):
    if all(f(x) for x in Ox):
        ans += [a2 - a1]
print(min(ans))
