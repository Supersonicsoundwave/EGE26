def conv(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(num):
    r = conv(num, 3)
    if num % 3 != 0:
        r = '1' + r + r[-3:]
    else:
        r += conv(sum(int(i) for i in r) * 8, 3)
    return int(r, 3)


ans = []
for n in range(1, 1000):
    ans += [(abs(1220 - f(n)), f(n))]
print(min(ans))
