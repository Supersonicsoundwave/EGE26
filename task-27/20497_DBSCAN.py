from math import dist


def anticenter(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return max(res)[1]


with open(r'.\files\27.19.A_20497.txt') as file:
    dots = [list(map(float, line.split())) for line in file]

eps = 0.5
cls = []
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl += [d]
                dots.remove(d)
    if len(cl) > 5:
        cls += [cl]

acs = [anticenter(cl) for cl in cls]

print(sum(x for x, y in acs) / 3 * 10_000)
print(sum(y for x, y in acs) / 3 * 10_000)


with open(r'.\files\27.19.B_20497.txt') as file:
    dots = [list(map(float, line.split())) for line in file]

eps = 5
cls = []
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl += [d]
                dots.remove(d)
    if len(cl) > 5:
        cls += [cl]
print([len(cl) for cl in cls])

acs = [anticenter(cl) for cl in cls]

print(sum(x for x, y in acs) / 5 * 10_000)
print(sum(y for x, y in acs) / 5 * 10_000)
