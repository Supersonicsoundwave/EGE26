from itertools import combinations


def f(x):
    B = 22 <= x <= 40
    C = 32 <= x <= 50
    A = a1 <= x <= a2
    return (not A) <= (B == C)


Oa = sorted([22, 40, 32, 50])
Ox = [n + 0.1 for n in Oa[:-1]]
ans = []
for a1, a2 in combinations(Oa, 2):
    if all(f(x) for x in Ox):
        ans += [a2 - a1]
print(min(ans))
