def conv(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1] if res else '0'


def f(n):
    r = conv(n, 4)
    if n % 4 == 0:
        r = '12' + r + conv(int(r[-1]) * 3, 4)
    else:
        r = '13' + r + '21'
    return int(r, 4)


ans = []
for n in range(1000):
    if f(n) > 50:
        ans += [f(n)]
print(min(ans))

