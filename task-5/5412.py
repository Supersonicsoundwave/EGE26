def f(n):
    r = hex(n)[2:]
    if r.count('b') % 2 == 0:
        r = '1' + r
    else:
        r += '1'
    return int(r, 16)


cnt = 0
for n in range(1, 100):
    if len(str(f(n))) == 2:
        cnt += 1
print(cnt)
