def convert(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(n):
    r = convert(n, 9)
    if r[0] == '7':
        r = r.replace('6', '*')
        r = r.replace('3', '6')
        r = r.replace('*', '3')
        r = '34' + r
    else:
        r = '3' + r[1:] + '45'
    return int(r, 9)


ans = []
for n in range(1, 10000):
    if f(n) < 2876:
        ans += [(f(n), n)]
print(max(ans))
