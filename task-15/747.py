from itertools import combinations


def f(x):
    P = 43 <= x <= 49
    Q = 44 <= x <= 53
    A = a1 <= x <= a2
    return (A <= P) or Q


Oa = sorted([43, 49, 44, 53])
Ox = [x + 0.5 for x in Oa[:-1]]
ans = []
for a1, a2 in combinations(Oa, r=2):
    if all(f(x) for x in Ox):
        ans += [a2 - a1]
print(max(ans))
