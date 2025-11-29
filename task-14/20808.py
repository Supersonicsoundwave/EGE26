def convert(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


ans = []
for x in range(2030, 0, -1):
    f = convert(7**170 + 7**100 - x, 7)
    ans += [(f.count('0'), x)]

print(max(ans))