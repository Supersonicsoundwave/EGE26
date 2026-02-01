def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    if len(d) > 1:
        return min(d) + max(d)
    return 0


cnt = 0
for n in range(800_001, 10**20):
    m = f(n)
    if m % 10 == 4:
        print(n, m)
        cnt += 1
        if cnt == 5:
            break
