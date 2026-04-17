from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_B_17834.txt') as file:
    dots = [tuple(map(float, line.replace(',', '.').split())) for line in file]

cl1 = [dot for dot in dots if dot[1] > -1.5 * dot[0] + 12]
cl2 = [dot for dot in dots if (dot[1] < -1.5 * dot[0] + 12) and (dot[1] > dot[0])]
cl3 = [dot for dot in dots if (dot[1] < -1.5 * dot[0] + 12) and (dot[1] < dot[0])]

cen1 = center(cl1)
cen2 = center(cl2)
cen3 = center(cl3)

print((cen1[0] + cen2[0] + cen3[0]) / 3 * 100)
print((cen1[1] + cen2[1] + cen3[1]) / 3 * 100)

