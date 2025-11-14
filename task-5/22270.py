from string import printable


def convert(x, q):
    ans = ''
    while x:
        ans += printable[x % q]
        x //= q
    return ans[::-1]


def f(n):
    r = convert(n, 4)
    if r[0] == '3':
        r = r.replace('3', '*')
        r = r.replace('1', '3')
        r = r.replace('*', '1')
        r += '21'
    else:
        r = '1' + r[1:] + '12'
    return int(r, 4)


ans = []
for n in range(1, 10000):
    if f(n) < 598:
        ans += [(n, f(n))]
print(max(ans))

