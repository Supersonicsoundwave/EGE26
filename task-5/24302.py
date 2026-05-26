def conv(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(n):
    r = conv(n, 3)
    if sum(int(x) for x in r) % 9 == 0:
        r += '2'
    else:
        r += conv(sum(int(x) for x in r) % 9, 3)
    return int(r, 3)


ans = []
for n in range(167, 1000):
    ans += [f(n)]

print(min(ans))
