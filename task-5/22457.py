from string import printable


def toq(x, q):
    ans = ''
    while x:
        ans += printable[x % q]
        x //= q
    return ans[::-1]


def f(n):
    r = toq(n, 7)
    if sum(map(int, r)) % 2 == 0:
        r += '555'
    else:
        r = '33' + r + '6'
    return int(r, 7)


for n in range(1000, 0, -1):
    if f(n) < 12717:
        print(n)
        break

