from itertools import combinations


def f(x):
    P = 15 <= x <= 33
    Q = 35 <= x <= 48
    A = a1 <= x <= a2
    return (A and not Q) <= (P or Q)


line = [x + eps for x in range(15, 48 + 1) for eps in (0, 0.1, 0.9)]
ans = []
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans += [a2 - a1]
print(max(ans))
