from string import printable


def convert(x, q):
    ans = ''
    while x:
        ans += printable[x % q]
        x //= q
    return ans[::-1]


def f(n):
    r = convert(n, 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += convert(sum(map(int, r)), 3)
    return int(r, 3)


ans = []
for n in range(1, 10000):
    if f(n) > 220:
        ans += [f(n)]
print(min(ans))
