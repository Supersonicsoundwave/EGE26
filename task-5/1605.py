def f(n):
    r = bin(2 + n)[2:]
    for i in range(2):
        r += str(r.count('1') % 2)
    return int(r, 2)


for n in range(1000, 0, -1):
    if f(n) < 61:
        print(n)
        break
