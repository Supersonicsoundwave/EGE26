from itertools import *


def f(x, y, z, w):
    return not (y <= (x == z)) and (w <= x)


for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    table = [(a1, 0, 0, a2),
             (0, a3, 0, a4),
             (a5, 1, a6, a7)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(*p, sep='')
