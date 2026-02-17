from functools import lru_cache


def f(n):
    return 3 * (g(n - 2) + 5)


@lru_cache(None)
def g(n):
    if n < 8:
        return 3 * n
    return g(n - 3) + 2


for i in range(50, 12_343 + 1):
    g(i)

print(f(12_345))
