from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 2025:
        return n
    return f(n + 1) - f(n + 2) + 7


for i in range(2025, 14, -1):
    f(i)

print(f(15) - f(24))
