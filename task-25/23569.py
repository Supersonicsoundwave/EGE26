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


cnt = 0
for n in range(6_086_055 + 1, 10**20):
    m = fact(n)
    if len(m) == 2 and all(str(x).count('6') == 1 for x in m):
        print(n, max(m))
        cnt += 1
        if cnt == 5:
            break


