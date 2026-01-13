from itertools import combinations


def f(x):
    P = 1 <= x <= 39
    Q = 23 <= x <= 58
    A = a1 <= x <= a2
    return (P <= (not Q)) <= (not A)


Oa = [1, 23, 39, 58]
Ox = [10, 30, 45]
ans = []
for a1, a2 in combinations(Oa, 2):
    if all(f(x) for x in Ox):
        ans += [a2 - a1]
print(max(ans))

