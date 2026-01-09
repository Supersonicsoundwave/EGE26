from itertools import combinations


def f(x):
    P = 12 <= x <= 28
    Q = 15 <= x <= 30
    A = a1 <= x <= a2
    return (P <= A) and (not Q or A)


line = [x + eps for x in range(12, 30 + 1) for eps in (0, 0.1, 0.9)]
ans = []
for a1, a2, in combinations(line, 2):
    if all(f(x) for x in line):
        ans += [a2 - a1]
print(min(ans))
