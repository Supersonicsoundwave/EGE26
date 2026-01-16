def convert(x, q):
    res = []
    while x:
        res += [x % q]
        x //= q
    return res[::-1]


f = convert(3*17**777 + 15*17**250 - 6*17**100 + 2, 17)
print(len(set([x for x in f if x % 2 == 0])))
