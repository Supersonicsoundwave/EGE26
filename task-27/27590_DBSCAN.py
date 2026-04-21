from math import dist


def anticenter(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return max(res)[1]


with open(r'.\files\27A_27590.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

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

print(sum(anticenter(min(cls, key=len))) * 10_000)
print(sum(anticenter(max(cls, key=len))) * 10_000)


with open(r'.\files\27B_27590.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

eps = 1
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

acs = [anticenter(cl) for cl in cls]

print(max(acs, key=lambda x: dist(x, (0, 0)))[0] * 10_000)
print(min(acs, key=lambda x: dist(x, (0, 0)))[1] * 10_000)
