def convert(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(n):
    r = convert(n, 3)
    if sum(map(int, r)) % 2 == 0:
        r = '1' + r + '2'
    else:
        r = '2' + r + '0'
    return int(r, 3)


ans = []
for n in range(1, 1000):
    if f(n) > 100:
        ans += [f(n)]
print(min(ans))
