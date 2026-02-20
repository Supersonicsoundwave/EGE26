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
            if is_prime(i):
                d |= {i}
            if is_prime(num // i):
                d |= {num // i}
    if len(d) > 3:
        d = sorted(d)
        m = sum(d[:2]) + sum(d[-2:])
        if m % 114 == 39:
            return m
    return 0


cnt = 0
for n in range(456_789 + 1, 10**20):
    if m := f(n):
        print(n, m)
        cnt += 1
        if cnt == 5:
            break
