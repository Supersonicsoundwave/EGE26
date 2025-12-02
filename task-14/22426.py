def convert(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


f = convert(15*343**2031 + 7*49**1142 - 3*7**111 + 7**222 - 16809, 7)
even = sum(map(lambda x: int(x in '0246'), f))
odd = sum(map(lambda x: int(x in '135'), f))
print(even - odd)
