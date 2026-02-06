def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if d:
        m = sum(d) // len(d)
        if m % 1000 == 313:
            return m
    return 0


cnt = 0
for n in range(700_000 - 1, 0, -1):
    if m := f(n):
        print(n, m)
        cnt += 1
        if cnt == 7:
            break
