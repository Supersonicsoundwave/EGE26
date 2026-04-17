from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_B_17915.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cluster1 = [dot for dot in dots if dot[0] < 12 and dot[1] > 16]
cluster2 = [dot for dot in dots if dot[0] > 23 and dot[1] > 15]
cluster3 = [dot for dot in dots if dot[0] > 15 and dot[1] < 11]
cluster4 = [dot for dot in dots if dot[0] < 15 and dot[1] < 9]

cen1 = center(cluster1)
cen2 = center(cluster2)
cen3 = center(cluster3)
cen4 = center(cluster4)

print((cen1[0] + cen2[0] + cen3[0] + cen4[0]) / 4 * 10_000)
print((cen1[1] + cen2[1] + cen3[1] + cen4[1]) / 4 * 10_000)
