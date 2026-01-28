def f(n):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '10' + r[:-2] + '00'
    else:
        r = '11' + r[:-2] + '11'
    return int(r, 2)


ans = []
for n in range(1, 30):
    ans += [f(n)]
print(max(ans))
