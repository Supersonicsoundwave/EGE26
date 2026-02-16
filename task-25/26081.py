st3 = [3**i for i in range(1, 15)]


def f(num):
    for i in range(1, num // 113 + 1, 2):
        ost = num - 113 * i
        if ost in st3:
            return st3.index(ost) + 1
    return 0


cnt = 0
for n in range(100_000, 1_000_000):
    if '0' not in str(n):
        if p := f(n):
            print(n, p)
            cnt += 1
            if cnt == 5:
                break
