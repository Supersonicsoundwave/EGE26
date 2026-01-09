from itertools import combinations


def f(x):
    B = 18 <= x <= 52
    C = 16 <= x <= 41
    A = a1 <= x <= a2
    return (B <= A) and (not C or A)


line = [x + eps for x in range(16, 52 + 1) for eps in (0, 0.1, 0.9)]
ans = []
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans += [a2 - a1]
print(min(ans))
