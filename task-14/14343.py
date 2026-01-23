def conv(x, q):
    res = []
    while x:
        res += [x % q]
        x //= q
    return res[::-1]


f = conv(5*343**2031 + 4*49**2142 - 3*7**111 + 7**222, 7)
print(sum(f))
