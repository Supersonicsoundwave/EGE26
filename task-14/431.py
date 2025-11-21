def convert(x, q):
    ans = []
    while x:
        ans += [x % q]
        x //= q
    return ans[::-1]


for x in range(100):
    num = 3*7**(x+1) + 13*7**(x+2) + 31*7**(3*x) + 7**(2*x)
    if sum(convert(num, 7)) == 18:
        print(x)
        break
