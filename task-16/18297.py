from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 10:
        return n - 1
    if n % 2 == 0:
        return 3 * n - 1 + f(n - 3)
    return 5 * n + 2 + f(n - 4)


for i in range(6, 4446):
    f(i)

print(f(4445) - f(4444))

