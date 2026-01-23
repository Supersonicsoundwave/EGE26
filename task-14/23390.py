def convert(x, q):
    res = []
    while x:
        res += [x % q]
        x //= q
    return res[::-1]


f = convert(17*125**453 + 117*5**231 - 3*5**13 - 2357, 125)
print(len([x for x in f if x <= 37]))

