def f(num):
    d = []
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d += [i, num // i]
    if len(d) == len(set(d)) == 4:
        return sorted(d, reverse=True)
    return []


for n in range(178_965, 178982 + 1):
    if d := f(n):
        print(*d)
