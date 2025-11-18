from string import printable


def convert(x, q):
    ans = ''
    while x:
        ans += printable[x % q]
        x //= q
    return ans[::-1]


def f(n):
    r = convert(n, 3)
    if sum(map(int, r)) % 2 == 0:
        r = '12' + r[2:] + '0'
    else:
        r = '10' + r[2:] + '2'
    return int(r, 3)


for n in range(1, 10000):
    if f(n) > 105:
        print(n)
        break
