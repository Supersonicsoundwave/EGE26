from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_23209.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

clA1 = [dot for dot in dots if dot[0] < 6]
clA2 = [dot for dot in dots if dot[0] > 6]

cenA1 = center(clA1)
cenA2 = center(clA2)

print(max(cenA1[0], cenA2[0]) * 10_000)
print(max(cenA1[1], cenA2[1]) * 10_000)


with open(r'.\files\27_B_23209.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

clB1 = [d for d in dots if 5 < d[1] < 10]
clB2 = [d for d in dots if 16 < d[1] < 21]
clB3 = [d for d in dots if 21 < d[1] < 26]

cenB1 = center(clB1)
cenB2 = center(clB2)
cenB3 = center(clB3)

print((cenB3[0] - cenB1[0]) * 10_000)
print((cenB3[1] - cenB1[1]) * 10_000)

cls = [clB1, clB2, clB3]
max_cen = center(max(cls, key=len))
min_cen = center(min(cls, key=len))

print((max_cen[0] - min_cen[0]) * 10_000)
print((max_cen[1] - min_cen[1]) * 10_000)
