def convert(x, q):
    res = []
    while x:
        res += [x % q]
        x //= q
    return res[::-1]


f = convert(2*2401**525 + 3*343**524 - 4*49**523 + 5*49**522 - 6*7**521 - 35, 49)
print(sum(map(lambda x: int(x <= 9), f)))