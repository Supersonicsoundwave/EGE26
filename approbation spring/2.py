from itertools import *


def f(x, y, z, w):
    return ((z == x) <= w) and (w <= (y and x))


for a1, a2, a3 in product((0, 1), repeat=3):
    table = [(1, 1, a1, 0),
             (1, a2, a3, 0),
             (1, 0, 1, 1)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(*p, sep='')

#########################################################################

print('x y z wS')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x, y, z, w):
                    print(x, y, z, w)

