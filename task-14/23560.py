def convert(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


for x in range(2400, 0, -1):
    f = convert(7*9**210 + 6*9**110 - x, 9)
    if f.count('0') == 100:
        print(x)
        break