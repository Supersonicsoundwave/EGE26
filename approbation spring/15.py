from itertools import combinations


def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return P <= ((Q and not A) <= (not P))


Oa = sorted([15, 40, 21, 63])
Ox = [x + 0.5 for x in Oa[:-1]]
ans = []
for a1, a2 in combinations(Oa, r=2):
    if all(f(x) for x in Ox):
        ans += [a2 - a1]
print(min(ans))
