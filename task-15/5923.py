from itertools import combinations


def f(x):
    P = 5 <= x <= 280
    Q = 295 <= x <= 400
    R = 375 <= x <= 450
    A = a1 <= x <= a2
    return (Q <= P) or ((not A) <= R)


Oa = sorted([5, 280, 295, 400, 375, 450])
Ox = [x + 0.5 for x in Oa[:-1]]
ans = []
for a1, a2 in combinations(Oa, 2):
    if all(f(x) for x in Ox):
        ans += [a2 - a1]
print(min(ans))
