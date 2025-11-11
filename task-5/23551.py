def f(n):
    r = f'{n:b}'
    if r.count('1') % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    return int(r, 2)


for n in range(10000, 0, -1):
    if f(n) < 30:
        print(n)
        break