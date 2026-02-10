def fact(num):
    m = []

    while num % 2 == 0:
        m += [2]
        num //= 2

    i = 3
    while i * i <= num:
        while num % i ==0:
            m += [i]
            num //= i
        i += 2

    if num > 2:
        m += [num]

    return m


def cond(lst):
    for i in lst:
        if lst.count(i) == 5:
            return i
    return 0


cnt = 0
for n in range(5_000_012, 10 ** 20, 100):
    m = fact(n)
    if dub := cond(m):
        print(n, dub)
        cnt += 1
        if cnt == 5:
            break



