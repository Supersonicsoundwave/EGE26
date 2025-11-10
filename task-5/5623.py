def f(n):
    r = f'{n:b}'
    if r.count('1') % 2 == 0:
        r = '1' + r[:-2] + '10'
    else:
        r = '10' + r[2:] + '1'
    return int(r, 2)


for n in range(1, 100):
    if f(n) > 202:
        print(n)
        break