def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 6:
        return sorted(d)[-7], len(d)
    return ()


cnt = 0
for n in range(400_000_000 + 1, 10**20):
    if d := f(n):
        print(*d)
        cnt += 1
        if cnt == 5:
            break
