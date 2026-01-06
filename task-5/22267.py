def convert(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(n):
    r = convert(n, 7)
    if r[-1] == '2':
        r = r.replace('3', '*')
        r = r.replace('1', '3')
        r = r.replace('*', '3')
        r = '21' + r
    else:
        r = '1' + r[1:] + '36'
    return int(r, 7)


ans = []
for n in range(1, 10000):
    if f(n) < 744:
        ans += [(f(n), n)]
print(max(ans, key=lambda x: (x[0], -x[1])))

