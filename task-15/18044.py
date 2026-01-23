from itertools import combinations


def f(x):
    M = 32 <= x <= 68
    N = 54 <= x <= 76
    A = a1 <= x <= a2
    return (not (M or N)) == (not A)


Oa = sorted([32, 68, 54, 76])
Ox = [x + 0.5 for x in Oa[:-1]]
ans = []
for a1, a2 in combinations(Oa, 2):
    if all(f(x) for x in Ox):
        ans += [a2 - a1]
print(min(ans))


