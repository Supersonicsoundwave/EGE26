from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_23209.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]
# print(len(dots))

eps = 1
cls = []
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl += [d]
                dots.remove(d)
    cls += [cl]

# print([len(cl) for cl in cls])

cens = [center(cl) for cl in cls]
print(max(cen[0] for cen in cens) * 10_000)
print(max(cen[1] for cen in cens) * 10_000)


with open(r'.\files\27_B_23209.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]
# print(len(dots))

eps = 2
cls = []
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl += [d]
                dots.remove(d)
    if len(cl) > 1:
        cls += [cl]

# print([len(cl) for cl in cls])

cens = [center(cl) for cl in cls]
max_c = center(max(cls, key=len))
min_c = center(min(cls, key=len))
print((max_c[0] - min_c[0]) * 10_000)
print((max_c[1] - min_c[1]) * 10_000)
