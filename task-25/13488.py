def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if sum(1 for x in d if x % 2 != 0) == 3:
        return [x for x in d if x % 2 != 0]
    else:
        return 0


for n in range(18782, 18822 + 1):
    F = f(n)
    if F:
        print(*sorted(F))




