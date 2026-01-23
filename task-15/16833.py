from itertools import combinations


def f(x):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = a1 <= x <= a2
    return (A and not Q) <= (P or Q)


lineA = [25, 73, 75, 118]
lineX = [60, 74, 100]
ans = []
for a1, a2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans += [a2 - a1]
print(max(ans))
