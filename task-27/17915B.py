from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_17915.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cluster1 = [dot for dot in dots if dot[0] < 7]
cluster2 = [dot for dot in dots if dot[0] > 7 and dot[1] < 23]
cluster3 = [dot for dot in dots if dot[0] > 7 and dot[1] > 23]

cen1 = center(cluster1)
cen2 = center(cluster2)
cen3 = center(cluster3)

print((cen1[0] + cen2[0] + cen3[0]) / 3 * 10_000)
print((cen1[1] + cen2[1] + cen3[1]) / 3 * 10_000)