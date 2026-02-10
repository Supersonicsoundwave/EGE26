from math import log2


def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) == 3:
        return max(d)
    return []


for n in range(int(106_732_567 ** .5), int(152_673_836 ** .5) + 1):
    if m := f(n ** 2):
        print(n ** 2, m)


