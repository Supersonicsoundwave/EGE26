from string import printable


def convert(x, q):
    res = ''
    while x:
        res += printable[x % q]
        x //= q
    return res[::-1]


f = convert(3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025, 25)
print(f.count('0'))