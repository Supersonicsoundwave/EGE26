def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


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
    m = fact(num)
    if len(m) == 3 and all(is_prime(mn) for mn in m):
        if sum(1 for mn in m if '3' in str(mn) and '5' in str(mn)) == 3:
            return max(m)
    return 0


cnt = 0
for n in range(3_600_000 + 1, 10 ** 20):
    if mm := f(n):
        print(n, mm)
        cnt += 1
        if cnt == 5:
            break
