def f(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    return int(r, 2)


ans = []
for n in range(1, 10000):
    if f(n) > 225:
        ans.append(f(n))
print(min(ans))
