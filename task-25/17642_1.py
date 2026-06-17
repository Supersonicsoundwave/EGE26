def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    d9 = list(filter(lambda x: x != 9 and x % 10 == 9, d))
    if d9:
        return min(d9)
    return 0


cnt = 0
for n in range(800_000 + 1, 10**20):
    if d9 := f(n):
        print(n, d9)
        cnt += 1
        if cnt == 5:
            break
