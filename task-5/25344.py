def conv(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(n):
    r = conv(n, 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += conv(sum(map(int, r)) * 3, 3)
    return int(r, 3)


ans = []
for n in range(1, 100000):
    if f(n) % 2 != 0 and f(n) > 208:
        ans  += [f(n)]
print(min(ans))
