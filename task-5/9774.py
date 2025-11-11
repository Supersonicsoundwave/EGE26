def toq(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(n):
    r = toq(n, 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += toq((n % 3) * 5, 3)
    return int(r, 3)


ans = []
for n in range(1, 10000):
    if f(n) > 133:
        ans += [f(n)]
print(min(ans))



