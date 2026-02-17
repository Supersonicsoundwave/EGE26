from functools import lru_cache


@lru_cache(None)
def f(n):
    if n > 40:
        return f(n - 4) + 3020
    return 3 * (g(n - 2) - 15)


@lru_cache(None)
def g(n):
    if n >= 301208:
        return 10 * n + 50
    return g(n + 7) - 21


for i in range(301208, 20, -1):
    g(i)

for i in range(30, 2026 + 1):
    f(i)

print(f(2026))
