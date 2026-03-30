def conv(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


for x in range(50, 0, -1):
    for y in range(50, 0, -1):
        f = 5**50 + 5**30 - 5**x - y - 5**y - x
        if f > 0:
            f = conv(f, 5)
            if f.count('0') == 10:
                print(x * y)
                break

