from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_29081.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[2:] == 'VII':
            stars += [dots[-1]]

cl1 = [d for d in dots if d[1] < 8]
cl2 = [d for d in dots if d[1] > 8]

st1 = [s for s in stars if s[1] < 8]
st2 = [s for s in stars if s[1] > 8]

cen1 = center(cl1)
cen2 = center(cl2)

dists = []

for s in st1:
    dists += [dist(cen1, s)]
for s in st2:
    dists += [dist(cen2, s)]

print(min(dists) * 10_000, max(dists) * 10_000)

###########################################################

cluster_1 = [[d for d in dots if d[1] < 8],
             [d for d in stars if d[1] < 8]]
cluster_2 = [[d for d in dots if d[1] > 8],
             [d for d in stars if d[1] > 8]]
clusters = [cluster_1, cluster_2]
centers = [center(cl[0]) for cl in clusters]

ans = [dist(s, centers[i]) for i in range(2) for s in clusters[i][1]]

print(min(ans) * 10_000, max(ans) * 10_000)

ans = [dist(s, center(cl[0])) for cl in clusters for s in cl[1]]

print(min(ans) * 10_000, max(ans) * 10_000)
