def convert(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(n):
    r = convert(n, 5)
    if r[-1] == '0':
        r = r.replace('1', '*')
        r = r.replace('4', '1')
        r = r.replace('*', '4')
        r = '33' + r
    else:
        r = '3' + r[1:] + '42'
    return int(r, 5)


ans = []
for n in range(1, 100000):
    if f(n) < 1922:
        ans += [(f(n), n)]
print(max(ans, key=lambda x: (x[0], -x[1])))
