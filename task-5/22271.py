def convert(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(n):
    r = convert(n, 8)
    if r[0] == '5':
        r = r.replace('2', '*')
        r = r.replace('1', '2')
        r = r.replace('*', '1')
        r = '11' + r
    else:
        r = '2' + r[1:] + '10'
    return int(r, 8)


ans = []
for n in range(1, 10000):
    if f(n) < 1354:
        ans += [(f(n), n)]
print(max(ans))
