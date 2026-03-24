def conv(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(n):
    r = conv(n, 5)
    if sum(int(i) for i in r) % 5 == 0:
        r = r.replace('0', '*')
        r = r.replace('1', '0')
        r = r.replace('*', '1')
        r += '14'
    else:
        r += '33'
        r = '44' + r[2:]
    return int(r, 5)


ans = []
for n in range(1, 1000):
    r = f(n)
    if r > 370:
        ans += [(r, n)]
print(min(ans))
