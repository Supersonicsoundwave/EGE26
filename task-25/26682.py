def fact(num):
    m = []
    while num % 2 == 0:
        m += [2]
        num //= 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            m += [i]
            num //= i
        i += 2

    if num > 2:
        m += [num]

    return m


def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) % 90 == 0:
        return True
    return False


cnt = 0
for n in range(5_200_000 + 1, 10**20):
    m = fact(n)
    if len(m) == 9 and f(n):
        print(n, max(m))
        cnt += 1
        if cnt == 5:
            break



