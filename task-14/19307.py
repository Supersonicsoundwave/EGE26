def convert(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


f = convert(15625**16 - 3125**3 * 25**19 + 625**4 - 2005, 5)
print(f.count('0'))