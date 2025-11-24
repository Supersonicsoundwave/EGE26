def convert(x, q):
    ans = ''
    while x:
        ans += str(x % q)
        x //= q
    return ans[::-1]


def f(n):
    r = convert(n, 3)
    if sum(map(int, r)) % 3 == 0:
        r += '212'
    else:
        r += convert(sum(map(int, r)) * 2, 3)
    return int(r, 3)


res = []
for n in range(1, 1000):
    if f(n) > 490:
        res += [f(n)]
print(min(res))