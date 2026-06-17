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
            d |= {num //i, i}
    prime_d = list(filter(is_prime, d))
    if len(prime_d) >= 2:
        return min(prime_d) + max(prime_d)
    return 0


cnt = 0
for n in range(5_400_000 + 1, 10**20):
    m = f(n)
    if m > 60_000 and str(m) == str(m)[::-1]:
        print(n, m)
        cnt += 1
        if cnt == 5:
            break
