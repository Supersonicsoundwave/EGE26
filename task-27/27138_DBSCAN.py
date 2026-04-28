from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27A_27138.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]


eps = 2
cls = []
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl += [d]
                dots.remove(d)
    cls += [cl]

cens = [center(cl) for cl in cls]

print(abs(cens[0][0] - cens[1][0]) * 10_000)
print(abs(cens[0][1] - cens[1][1]) * 10_000)


with open(r'.\files\27B_27138.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cls = []
eps = 1
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl += [d]
                dots.remove(d)
    if len(cl) > 1:
        cls += [cl]
cls = sorted(cls, key=len)

print(max(cls[1])[0] * 10_000)

cl1 = cls[0]
cl2 = cls[1]
cl3 = cls[2]

res = []
for dot in cl1:
    sum_dist = sum(dist(dot, d) for d in cl2 + cl3)
    res += [(sum_dist, dot)]
for dot in cl2:
    sum_dist = sum(dist(dot, d) for d in cl1 + cl3)
    res += [(sum_dist, dot)]
for dot in cl3:
    sum_dist = sum(dist(dot, d) for d in cl2 + cl1)
    res += [(sum_dist, dot)]
mdd = max(res)[1]
print((mdd[0] + mdd[1]) * 10_000)