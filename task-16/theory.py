from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 2025:
        return n
    return f(n + 1) - f(n + 2) + 7


for i in range(2025, 14, -1):
    f(i)


# или
ans = [0] * 2030
ans[2026] = 2026
ans[2025] = 2025
for i in range(2024, 0, -1):
    ans[i] = ans[i + 1] - ans[i + 2] + 7

print(ans[15] - ans[24])

