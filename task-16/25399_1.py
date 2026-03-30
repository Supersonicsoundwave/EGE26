from functools import lru_cache


@lru_cache(None)
def f(n): # 2049 -> 127
    if n >= 128:
        return f(n - 5) + 1092
    return 5 * g(n - 7) + 29


@lru_cache(None)
def g(n): # 120 -> 303729
    if n > 303728:
        return n - 15
    return g(n + 8) / 2 - 109


for i in range(303800, 100, -1):
    g(i)

for i in range(127, 2050):
    f(i)

print(f(2049))

############################################
F = [0] * 2050
G = [0] * 303800

for i in range(303800 - 1, -1, -1):
    if i > 303728:
        G[i] = i - 15
    else:
        G[i] = G[i + 8] / 2 - 109

for i in range(7, 2050):
    if i >= 128:
        F[i] = F[i - 5] + 1092
    else:
        F[i] = 5 * G[i - 7] + 29

print(F[2049])
