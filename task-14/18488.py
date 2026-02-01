def conv(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


for x in range(1, 1000):
    f = conv(7**666 + 7**333 + 49**x - 343, 7)
    if f.count('6') == 49:
        print(x)
        break


