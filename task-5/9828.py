def toq(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


def f(n):
    r = toq(n, 3)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r += toq((n % 3) * 4, 3)
    return int(r, 3)


for n in range(1000, 0, -1):
    if f(n) < 199:
        print(n)
        break
