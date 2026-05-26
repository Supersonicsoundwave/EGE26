from functools import lru_cache


def f(n):
    return 3 * g(n - 3) + 7


@lru_cache(None)
def g(n):
    if n <= 20:
        return n + 2
    return g(n - 3) + 1


for i in range(17, 37808):
    g(i)

print(f(37_811))
