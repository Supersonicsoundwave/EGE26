def f(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += bin(r.count('1'))[2:]
    else:
        r = '1' + r + '101'
    return int(r, 2)


for n in range(1, 1000):
    if f(n) > 350:
        print(n)
        break
