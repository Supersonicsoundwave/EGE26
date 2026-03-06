def f(n):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += bin((n % 3) * 3)[2:]
    return int(r, 2)


ans = []
for n in range(1, 1000):
    if 120 <= f(n) <= 140:
        ans += [(abs(130 - f(n)), n)]
print(sorted(ans, key=lambda x: (x[0], -x[1])))
# 31
