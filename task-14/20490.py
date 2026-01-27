def conv(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


for x in range(2005, 0, -1):
    f = conv(4**163*5 + 12**62 - x, 5)
    if f.count('1') < f.count('4'):
        print(x)
        break
