from itertools import *


def f(x, y, z, w):
    return ((z <= x) and (x <= y)) or (w == (z or x))


for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    table = [(a1, 1, a2, a3),
             (a4, a5, 1, 1),
             (a6, 1, a7, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p, sep='')
