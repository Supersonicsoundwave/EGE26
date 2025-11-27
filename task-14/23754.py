from string import printable


def convert(x, q):
    res = ''
    while x:
        res += printable[x % q]
        x //= q
    return res[::-1]


for x in range(3000, 0, -1):
    f = convert(9*11**210 + 8*11**150 - x, 11)
    if f.count('0') == 60:
        print(x)
        break