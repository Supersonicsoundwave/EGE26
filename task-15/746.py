from itertools import combinations


def f(x):
    P = 12 <= x <= 26
    Q = 30 <= x <= 53
    A = a1 <= x <= a2
    return (A <= P) or Q


line = [x + eps for x in range(12, 54) for eps in (0, 0.1, 0.9)]
ans = []
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(max(ans))
