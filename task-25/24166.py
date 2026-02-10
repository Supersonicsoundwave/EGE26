def f(num):
    m = []

    while num % 2 == 0:
        m += [2]
        num //= 2

    i = 3
    while i * i < num:
        while num % i == 0:
            m += [i]
            num //= i
        i += 2

    if num > 2:
        m += [num]

    if len(m) == 4:
        sm = str(sum(m))
        if sm == sm[::-1]:
            return sm
    return ''


cnt = 0
for n in range(7_305_678 + 1, 10**20):
    if sm := f(n):
        print(n, sm)
        cnt += 1
        if cnt == 5:
            break




