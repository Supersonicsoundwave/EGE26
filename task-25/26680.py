def fact(num):
    d = []
    i = 3
    while i * i < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


cnt = 0
for n in range(5_000_001, 10**20, 2):
    d = fact(n)
    if len(d) == 2 and len(set(d)) == 2 and is_prime(abs(d[1] - d[0])):
        print(n, max(d))
        cnt += 1
        if cnt == 5:
            break

