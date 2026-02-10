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

    if len(m) == 5:
        if sum(1 for x in m if '5' in str(x)) == 5:
            return max(m)
    return 0


cnt = 0
for n in range(13_475_124 + 1, 10**20):
    if m := f(n):
        print(n, m)
        cnt += 1
        if cnt == 5:
            break
