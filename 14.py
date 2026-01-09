def convert(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]


ans = []
for x in range(10, 70000 + 1):
    f = convert(5**2025 + 5**400 - x, 5)
    ans += [(f.count('4'), x)]
print(max(ans))