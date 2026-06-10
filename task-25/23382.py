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
    while i ** 2 <= num:
        while num % i == 0:
            if is_prime(i) and '2' in str(i):
                m += [i]
            num //= i
        i += 2

    if num > 2 and is_prime(num) and '2' in str(num):
        m += [num]

    if len(m) == 2:
        return max(m)
    return 0


cnt = 0
for num in range(6_651_220 + 1, 10**20):
    if m := fact(num):
        print(num, m)
        cnt += 1
        if cnt == 5:
            break
