from itertools import combinations


def f(x):
    P = 66 <= x <= 67
    O = 32 <= x <= 125
    T = 30 <= x <= 491
    A = a1 <= x <= a2
    return (not A) <= (P or not O or not T)


Oa = sorted([66, 67, 32, 125, 30, 491])
Ox = [x + 0.5 for x in Oa[:-1]]
ans = []
for a1, a2 in combinations(Oa, 2):
    if all(f(x) for x in Ox):
        ans += [a2 - a1]
print(min(ans))
