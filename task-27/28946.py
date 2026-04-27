from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_28946.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cl1 = [d for d in dots if d[1] > 16]
cl2 = [d for d in dots if d[1] < 16]

cen1 = center(cl1)
cen2 = center(cl2)

max_cl = max(cl1, cl2, key=len)
max_cen = center(max_cl)
A1 = sum(1 for d in max_cl if d[1] < max_cen[1])

A2 = abs(cen1[0] - cen2[0])

print(A1, A2 * 10_000)


with open(r'.\files\27_B_28946.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cl1 = [d for d in dots if d[1] > 21]
cl2 = [d for d in dots if d[1] < 21 and d[0] < 24]
cl3 = [d for d in dots if d[0] > 24]
cls = sorted([cl1, cl2, cl3], key=len)

min_cl = cls[0]
min_cen = center(min_cl)
B1 = sum(1 for d in min_cl if (min_cen[0] - 0.9 < d[0] < min_cen[0] + 0.9) and \
         (min_cen[1] - 0.9 < d[1] < min_cen[1] + 0.9))

mid_cen = center(cls[1])
max_cen = center(cls[2])
B2 = abs(mid_cen[1] - max_cen[1])

print(B1, B2 * 10_000)

