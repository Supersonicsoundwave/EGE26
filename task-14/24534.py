def conv(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


ans = []
for x in range(1, 11500 + 1):
    f = conv(7**270 + 7**170 + 7**70 - x, 7)
    ans += [(f.count('0'), x)]
print(max(ans))
