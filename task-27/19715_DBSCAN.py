from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27.21.A_19715.txt') as file:
    dots = [list(map(float, line.split())) for line in file]

eps = 1
cls = []
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl += [d]
                dots.remove(d)
    if len(cl) > 4:
        cls += [cl]

centers = [center(cl) for cl in cls]

print(sum(cen[0] for cen in centers) / 2 * 10_000)
print(sum(cen[1] for cen in centers) / 2 * 10_000)


with open(r'.\files\27.21.B_19715.txt') as file:
    dots = [list(map(float, line.split())) for line in file]
# print(len(dots))

eps = 4
cls = []
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl += [d]
                dots.remove(d)
    if len(cl) > 4:
        cls += [cl]

# print([len(cl) for cl in cls], sum(len(cl) for cl in cls))
centers = [center(cl) for cl in cls]

print(sum(cen[0] for cen in centers) / 4 * 10_000)
print(sum(cen[1] for cen in centers) / 4 * 10_000)

