def convert(x, q):
    ans = []
    while x:
        ans += [x % q]
        x //= q
    return ans[::-1]


num = 51*7**12 - 7**3 - 22
print(sum(convert(num, 7)))