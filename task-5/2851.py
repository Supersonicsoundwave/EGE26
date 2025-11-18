def f(n):
    r = bin(n)[2:]
    a = r[1::2].count('1')
    b = r[::2].count('0')
    return abs(a - b)


for n in range(2, 10000):
    if f(n) == 5:
        print(n)
        break