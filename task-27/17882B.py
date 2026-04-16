from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_B_17882.txt') as file:
    dots = [tuple(map(float, i.split())) for i in file]

cluster1 = [dot for dot in dots if dot[1] > 7]
cluster2 = [dot for dot in dots if 3 < dot[1] < 7]
cluster3 = [dot for dot in dots if dot[1] < 3]

center1 = center(cluster1)
center2 = center(cluster2)
center3 = center(cluster3)

print(int((center1[0] + center2[0] + center3[0]) / 3 * 10_000))
print(int((center1[1] + center2[1] + center3[1]) / 3 * 10_000))

