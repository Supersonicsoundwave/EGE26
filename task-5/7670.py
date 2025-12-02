def f(n):
    r = hex(n)[2:]
    r = r.replace('a', '1')
    if sum(map(lambda x: int(x in '02468ace'), r)) > 2:
        r += 'b'
    else:
        r = 'f' + r
    return int(r, 16)


ans = []
for n in range(151, 10000):
    if f(n) > 3500:
        ans += [(f(n), n)]
print(min(ans))
