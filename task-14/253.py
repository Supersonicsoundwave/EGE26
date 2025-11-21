def convert(x, q):
    ans = []
    while x:
        ans += [x % q]
        x //= q
    return ans[::-1]


for n in range(2, 100):
    if convert(41, n)[-1] == 2 and convert(131, n)[-1] == 1:
        print(n)
        break
