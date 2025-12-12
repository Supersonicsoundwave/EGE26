def f(n):
    r = bin(n)[2:]
    if r.count('0') % 2 == 0:
        r = '1' + r + '1'
    else:
        r = '10' + r
    return int(r, 2)


ans = []
for n in range(1, 100000):
    if f(n) < 100:
        ans.append(f(n))
print(max(ans))
