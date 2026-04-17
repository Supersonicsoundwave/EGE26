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
        i += 2

    if num > 2:
        res += [num]

    return res


def f(num):
    m = fact(num)
    if len(m) == 3:
        if sum(1 for mn in m if '3' in str(mn) or '4' in str(mn)) == 3:
            return max(m)
    return 0


cnt = 0
for n in range(6_300_000 + 1, 10 ** 20):
    if mm := f(n):
        print(n, mm)
        cnt += 1
        if cnt == 5:
            break
