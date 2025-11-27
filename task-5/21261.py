def convert(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(n):
    r = convert(n, 4)
    if sum(map(int, r)) % 3 == 0:
        r = r.replace('0', '*')
        r = r.replace('2', '0')
        r = r.replace('*', '2')
        r = '32' + r
    else:
        r += '33'
        r = r[0] + '10' + r[3:]
    return int(r, 4)


ans = []
for n in range(1, 10000):
    if f(n) > 320:
        ans += [(n, f(n))]

ans.sort(key=lambda x: (x[-1], -x[0]))
print(ans[0])


