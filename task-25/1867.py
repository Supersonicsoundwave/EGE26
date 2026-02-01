def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):  # находим все делители, кроме 1 и самого числа
        if num % i == 0:
            d |= {i, num // i}

    for i in sorted(d):  # находим минимальный делитель оканчивающийся на 8, не являющийся 8кой
        if i % 10 == 8 and i != 8:
            return i
    return 0  # если такого нет возвращаем 0


cnt = 0
for n in range(500_001, 10**20):
    F = f(n)
    if F:
        print(n, F)
        cnt += 1
        if cnt == 5:
            break

