from itertools import combinations


def f(x):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = a1 <= x <= a2
    return (not (C or J)) <= (not A)

lineA = [48, 83, 94, 100]
lineX = [49, 87, 95]

ans = []
for a1, a2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans += [a2 - a1]
print(max(ans))
