def conv(x, q):
    res = []
    while x:
        res += [x % q]
        x //= q
    return res[::-1]


ans = []
for x in range(1, 9430 + 1):
    f = conv(39**483 + 39**235 - x, 39)
    ans += [f.count(0)]
print(max(ans))
