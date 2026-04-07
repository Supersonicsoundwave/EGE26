def f(num):
    d11 = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if i % 100 == 11 and i != 11:
                d11 |= {i}
            if num // i % 100 == 11 and num // i != 11:
                d11 |= {num // i}
    if d11:
        return min(d11)
    return 0


cnt = 0
for n in range(1_350_050 + 1, 10 ** 20):
    if d11 := f(n):
        print(n, d11)
        cnt +=1
        if cnt == 5:
            break
