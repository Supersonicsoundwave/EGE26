def mult(st):
    ans = 1
    for num in st:
        ans *= num
    return ans


def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    sm = sum(d)
    mlt = mult(d)
    if sm % 2 == mlt % 2 == 1 and len(d) > 10:
        return len(d)
    return 0


cnt = 0
for n in range(800_000 + 1, 10**20):
    if l := f(n):
        print(n, l)
        cnt += 1
        if cnt == 6:
            break

