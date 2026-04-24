from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27A_18625.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cls = []
eps  = 1
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl += [d]
                dots.remove(d)
    if len(cl) > 4:
        cls += [cl]

cens = [center(cl) for cl in cls]

print(sum(x for x, y in cens) / len(cens) * 100_000)
print(sum(y for x, y in cens) / len(cens) * 100_000)


with open(r'.\files\27B_18625.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cls = []
eps  = 1
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl += [d]
                dots.remove(d)
    if len(cl) > 5:
        cls += [cl]

cens = [center(cl) for cl in cls]

print(sum(x for x, y in cens) / len(cens) * 100_000)
print(sum(y for x, y in cens) / len(cens) * 100_000)
