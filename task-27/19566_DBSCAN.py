from math import dist


def anticenter(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return max(res)[1]


with open(r'.\files\27.17.A_19566.txt') as file:
    dots= [list(map(float, line.split())) for line in file]

cls = []
eps = 1
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl += [d]
                dots.remove(d)
    if len(cl) > 4:
        cls += [cl]

acs = [anticenter(cl) for cl in cls]

print(sum(x for x, y in acs) / len(acs) * 10_000)
print(sum(y for x, y in acs) / len(acs) * 10_000)


with open(r'.\files\27.17.B_19566.txt') as file:
    dots= [list(map(float, line.split())) for line in file]

cls = []
eps = 1
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl += [d]
                dots.remove(d)
    if len(cl) > 10:
        cls += [cl]

acs = [anticenter(cl) for cl in cls]

print(sum(x for x, y in acs) / len(acs) * 10_000)
print(sum(y for x, y in acs) / len(acs) * 10_000)
