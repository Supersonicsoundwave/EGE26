def f(n):
    r = bin(n)[2:]
    r = r.replace('0', '00')
    r = r.replace('1', '11')
    return int(r, 2)


ans = []
for n in range(1, 1000):
    if f(n) > 63:
        ans += [f(n)]
print(min(ans))
