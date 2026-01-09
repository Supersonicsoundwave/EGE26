from itertools import combinations


def f(x):
    P = 5 <= x <= 30
    Q = 14 <= x <= 23
    A = a1 <= x <= a2
    return (P == Q) <= (not A)


# line = [x + eps for x in range(5, 31) for eps in (0, 0.1, 0.9)]
# ans = []
# for a1, a2 in combinations(line, 2):
#     if all(f(x) for x in line):
#         ans += [a2 - a1]
# print(max(ans))

Oa = [5, 14, 23, 30]
Ox = [10, 20, 27]
ans = []
for a1, a2 in combinations(Oa, 2):
    if all(f(x) for x in Ox):
        ans += [a2 - a1]
print(max(ans))

