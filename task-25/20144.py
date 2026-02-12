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
        r = max(d) - min(d)
        if r > 1000 and r % 3 == 0:
            return r
    return 0


cnt = 0
for n in range(3_333_337 + 1, 10**20):
    if r := f(n):
        print(n, r)
        cnt += 1
        if cnt == 5:
            break

