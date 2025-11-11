def f(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    return int(r, 2)


ans = []
for n in range(1, 12 + 1):
    ans.append(f(n))
print(max(ans))





