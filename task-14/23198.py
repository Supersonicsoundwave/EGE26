def conv(num, q):
    res = ''
    while num:
        res += str(num % q)
        num //= q
    return res[::-1]


for x in range(1, 3000 + 1):
    f = conv(9 ** 150 + 9 ** 30 - x, 9)
    if f.count('0') == 122:
        print(x)
        break
