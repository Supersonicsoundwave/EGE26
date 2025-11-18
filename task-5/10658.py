from string import printable


def convert(x, q):
    ans = ''
    while x:
        ans += printable[x % q]
        x //= q
    return ans[::-1]


def f(n):
    r = convert(n, 3)
    if sum(map(lambda x: int(int(x) % 2 == 0), r)) > sum(map(lambda x: int(int(x) % 2 != 0), r)):
        r = '22' + r
    else:
        r = '11' + r
    return int(r, 3)


ans = []
for n in range(11, 10000):
    if f(n) > 100:
        ans += [f(n)]
print(min(ans))
