from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 6:
        return n
    return (3 * n - 2) * f(n - 5)


for i in range(1, 20568 + 1):
    f(i)

print((f(20568) - 51702 * f(20563)) / f(20553))

