from string import printable


def conv(x, q):
    res = ''
    while x:
        res += printable[x % q]
        x //= q
    return res[::-1]


for x in range(1, 27000):
    f =  conv(3*27**9 + 2*27**6 + 27**3 - x, 27)
    if f.count('0') == 6:
        print(x)
        break