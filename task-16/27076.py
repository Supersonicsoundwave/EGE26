from functools import lru_cache


@lru_cache(None)
def f(n): # 2026 -> 42 -> g
    if n < 43:
        return g(n + 4)
    return 2 * f(n - 2) - f(n - 4) + 2


@lru_cache(None)
def g(n): # 46 -> 11_241 -> q
    if n < 11_240:
        return g(n + 3) + 2
    return q(n)


@lru_cache(None)
def q(n): # 11_241 -> 20
    if n < 21:
        return n + 4
    return q(n - 4) + 2


for i in range(20, 11_241):
    q(i)

for i in range(11_241, 45, -1):
    g(i)

print(f(2026))

#####################################################

F = [0] * 2300
G = [0] * 12_001
Q = [0] * 12_001

for i in range(12_000 + 1):
    if i < 21:
        Q[i] = i + 4
    else:
        Q[i] = Q[i - 4] + 2

for i in range(12_000, -1, -1):
    if i < 11_240:
        G[i] = G[i + 3] + 2
    else:
        G[i] = Q[i]

for i in range(2300):
    if i < 43:
        F[i] = G[i + 4]
    else:
        F[i] = 2 * F[i - 2] - F[i - 4] + 2

print(F[2026])
