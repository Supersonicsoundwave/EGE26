def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    if d:
        m = sum(d)
        if is_prime(m % 100_000):
            return m
    return 0


cnt = 0
for n in range(1_273_547 + 1, 10**20):
    if m := f(n):
        print(n, m)
        cnt += 1
        if cnt == 5:
            break
