from itertools import product, permutations


def f(w, x, y, z):
    return (x and not y) or (y == z) or not w


for a, b, c, d in product((0, 1), repeat=4):
    table = [
        (a, b, 0, 0),
        (1, 0, c, 0),
        (1, 0, 1, d)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p, sep='')
