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
    return sum(d)


cnt = 0
for n in range(32_500_000 + 1, 10**20):
    s = f(n)
    if s and s % 145 == 0:
        print(n, s)
        cnt += 1
        if cnt == 7:
            break
