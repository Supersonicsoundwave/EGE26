def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    s = sum(d)
    if s % 100 == 23:
        return s
    return 0


for n in range(1_000, 10_000):
    if s := f(n):
        print(n, s)
