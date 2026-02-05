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
    if len(d) > 1:
        m = min(d) + max(d)
        if m > 2000 and m % 10 == 8:
            return m
    return 0


cnt = 0
for n in range(1_200_000 + 1, 10**20):
    if m := f(n):
        print(n, m)
        cnt += 1
        if cnt == 5:
            break
