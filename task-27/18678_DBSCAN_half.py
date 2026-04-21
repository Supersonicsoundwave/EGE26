from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27A_18678.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cl1 = [dot for dot in dots if dot[1] < 2]
cl2 = [dot for dot in dots if dot[1]> 2 and 1 < dot[0] < 6]

cen1 = center(cl1)
cen2 = center(cl2)

print((cen1[0] + cen2[0]) / 2 * 100_000)
print((cen1[1] + cen2[1]) / 2 * 100_000)


with open(r'.\files\27B_18678.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cls = []
eps = 1
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(d, dot) < eps:
                cl += [d]
                dots.remove(d)
    if len(cl) >= 30:
        cls += [cl]

cs = [center(cl) for cl in cls]

print(sum(x for x, y in cs) / 3 * 100_000)
print(sum(y for x, y in cs) / 3 * 100_000)
