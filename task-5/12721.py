def f(n):
    r = oct(n)[2:]
    if sum(map(lambda x: int(int(x) % 2 == 0), r)) % 2 != 0:
        r = r[-3:] +'46'
    else:
        r = oct((n % 8) * 5)[2:] + r
    return int(r, 8)


ans = []
for n in range(80, 1000):
    ans += [f(n)]
print(min(ans))

