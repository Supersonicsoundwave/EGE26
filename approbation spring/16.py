from functools import lru_cache


def f(n): # 12_345
    return 3 * (g(n - 2) + 5)


@lru_cache(None)
def g(n): # 12_343 -> 5
    if n < 8:
        return 3 * n
    return g(n - 3) + 2


for i in range(5, 12_344):
    g(i)

print(f(12_345))

#########################################

G = [0] * 12_350
for i in range(12_350):
    if i < 8:
        G[i] = 3 * i
    else:
        G[i] = G[i - 3] + 2

print(3 * (G[12_345 - 2] + 5))

