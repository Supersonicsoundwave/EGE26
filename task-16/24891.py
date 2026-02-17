from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 10:
        return n
    return n - 7 + f(n - 21)


for i in range(10, 185_734 + 1):
    f(i)

print((f(185_734) - f(185_650)) / f(40))
