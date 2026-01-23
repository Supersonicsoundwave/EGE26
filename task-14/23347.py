def conv(x, q):
    res = []
    while x:
        res += [x % q]
        x //= q
    return res[::-1]


f = conv(15*49**237 + 37*343**500 - 14*7**35, 49)
print(len([x for x in f if x > 15]))

