def treug(n, m, k):
    return n + m > k and n + k > m and m + k > n


def f(x):
    return not ((treug(x, 11, 18) == (not (max(x, 5) > 68))) and treug(x, a, 5))


for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break