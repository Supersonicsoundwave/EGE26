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
            if is_prime(i) and i % 10 == 7:
                d |= {i}
            if is_prime(num // i)and (num // i) % 10 == 7:
                d |= {num // i}
    if d:
        z = sum(d) // len(d)
        if z % 111 == 0:
            return z
    return 0


cnt = 0
for n in range(750_000, - 1, -1):
    if Z := f(n):
        print(n, Z)
        cnt += 1
        if cnt == 5:
            break
