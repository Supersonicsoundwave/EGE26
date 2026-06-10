def f(n):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r += '1'
        r = '10' + r[2:]
    else:
        r += '0'
        r = '11' + r[2:]
    return int(r, 2)


ans = []
for n in range(1, 16):
    ans += [f(n)]
print(max(ans))
