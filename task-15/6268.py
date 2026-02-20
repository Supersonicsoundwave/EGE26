from itertools import combinations


def f(x):
    B = 23 <= x <= 37
    C = 41 <= x <= 73
    A = a1 <= x <= a2
    return ((not B) <= C) <= A


Oa = sorted([23, 37, 41, 73])
Ox = [x + 0.5 for x in Oa[:-1]]
for a1, a2 in combinations(Oa, r=2):
    if all(f(x) for x in Ox):
        print(a2 - a1)
