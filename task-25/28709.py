def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


def fact(num):
    res = []
    while num % 2 == 0:
        res += [2]
        num //= 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            res += [i]
            num //= i

    if num > 2:
        res += [num]

    return res


def f(num):
    m = fact(num)
    if len(m) == 3 and all(is_prime(mn) for mn in m):
        if sum(1 for mn in m if '3' in str(mn) or '4' in str(mn)) == 3:
            return max(m)
    return 0


cnt = 0
print(fact(6300051))
# for n in range(6_300_000 + 1, 10 ** 20):
#     if mm := f(n):
#         print(n, mm)
#         cnt += 1
#         if cnt == 5:
#             break
#

