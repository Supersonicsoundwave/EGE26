def conv(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(n):
    r = conv(n, 4)
    if n % 4 == 0:
        r += r[:2]
    else:
        r += conv((n % 4) * 4, 4)
    return int(r, 4)


ans = []
for n in range(1, 1000):
    r = f(n)
    if r > 291:
        ans += [r]
print(min(ans))
