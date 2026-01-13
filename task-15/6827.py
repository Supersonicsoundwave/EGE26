from itertools import combinations


def f(x):
    P = 257 <= x <= 1000
    Q = 5 <= x <= 100
    R = 99 <= x <= 258
    A = a1 <= x <= a2
    return (A <= R) and ((not (A <= P)) <= Q)


Oa = [5, 99, 100, 257, 258, 1000]
Ox = [50, 99.5, 200, 257.5, 300]
ans = []
for a1 in Oa:
    for a2 in Oa:
        if a2 >= a1:
            if all(f(x) for x in Ox):
                ans += [a2 - a1]
print(min(ans))
