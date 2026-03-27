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
    if len(m) == 2 and all(is_prime(i) for i in m):
        if all(str(i).count('5') == 1 for i in m):
            return max(m)
    return 0


cnt = 0
for n in range(1_324_727 + 1, 10**20):
    if mn := f(n):
        print(n, mn)
        cnt += 1
        if cnt == 5:
            break


