from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_17882.txt') as file:
    dots = [tuple(map(float, i.split())) for i in file]

cluster1 = [dot for dot in dots if dot[0] < 1]
cluster2 = [dot for dot in dots if dot[0] > 1]

center1 = center(cluster1)
center2 = center(cluster2)
print(int((center1[0] + center2[0]) / 2 * 10_000))
print(int((center1[1] + center2[1]) / 2 * 10_000))
