from itertools import *


def f(x, y, z, w):
    return ((x or y) <= z) or (y == w) or z


for a, b, c, d in product((0, 1), repeat=4):
    table = [
        (0, 1, a, b),
        (1, c, 1, 0),
        (d, 1, 1, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p, sep='')