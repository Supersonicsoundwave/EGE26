# from itertools import *
#
#
# def f(x, y, z, w):
#     return (z <= y) or ((w <= x) <= y)
#
#
# for a1, a2, a3, a4, a5, a6 in product((0, 1), repeat=6):
#     table = [
#         (a1, 0, 0, a2),
#         (a3, a4, 1, a5),
#         (a6, 1, 1, 1)
#     ]
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
#                 print(*p, sep='')

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (z <= y) or ((w <= x) <= y)
                if not f:
                    print(x, y, z, w)

