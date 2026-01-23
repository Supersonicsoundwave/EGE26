from itertools import combinations


def f(x):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a1 <= x <= a2
    return (not ((not P) <= Q)) <= (A <= ((not Q) <= P))


line = [x + exp for x in range(13, 24) for exp in (0, 0.1, 0.9)]
ans = []
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans += [a2 - a1]
print(max(ans))