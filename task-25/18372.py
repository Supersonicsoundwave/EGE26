def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    d |= {1}
    a = sum(d) // len(d)
    if a % 100 == 12:
        return a
    return 0


cnt = 0
for n in range(770_000 - 1, 0, -1):
    if a := f(n):
        print(n, a)
        cnt += 1
        if cnt == 5:
            break
