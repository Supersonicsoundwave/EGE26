from itertools import *


def f(x, y, z, w):
    return (z == (not x)) <= ((w <= (not y)) and (y <= x))


for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    table = [(1, 1, 1, 0),
             (a1, a2, 0, 0),
             (a3, 0, a4, a5)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 0, 0]:
                print(*p, sep='')
