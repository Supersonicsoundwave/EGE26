def convert(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[:-1]


for x in range(1, 2300):
    f = convert(7**350 + 7**150 - x, 7)
    if f.count('0') == 200:
        print(x)