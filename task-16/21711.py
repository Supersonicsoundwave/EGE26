from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 20:
        return n
    return (n - 6) * f(n - 7)


for i in range(13, 47872 + 1):
    f(i)

print((f(47_872) - 290 * f(47_865)) / f(47_858))

