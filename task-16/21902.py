from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 2025:
        return n
    return n * 2 + f(n + 2)


for i in range(2026, 80, -1):
    f(i)

print(f(82) - f(81))
