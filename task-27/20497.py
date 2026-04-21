from math import dist


def anticenter(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return max(res)[1]


with open(r'.\files\27.19.A_20497.txt') as file:
    dots = [list(map(float, line.split())) for line in file]

cl1 = [d for d in dots if d[0] < 0 and d[1] < 0]
cl2 = [d for d in dots if d[0] > 0.5 and -6 < d[1] < 0]
cl3 = [d for d in dots if -1 < d[0] < 1.5 and 0 < d[1] < 6]

cls = [cl1, cl2, cl3]
acs = [anticenter(cl) for cl in cls]

print(sum(x for x, y in acs) / 3 * 10_000)
print(sum(y for x, y in acs) / 3 * 10_000)


with open(r'.\files\27.19.B_20497.txt') as file:
    dots = [list(map(float, line.split())) for line in file]

cl1 = [d for d in dots if d[0] < -35 and d[1] < 30]
cl2 = [d for d in dots if -25 < d[0] < -9 and d[1] < 30]
cl3 = [d for d in dots if 0 < d[0] < 20 and d[1] < 30]
cl4 = [d for d in dots if -39 < d[0] < -23 and d[1] > 40]
cl5 = [d for d in dots if -11 < d[0] < 5 and d[1] > 40]

cls = [cl1, cl2, cl3, cl4, cl5]
acs = [anticenter(cl) for cl in cls]

print(sum(x for x, y in acs) / 5 * 10_000)
print(sum(y for x, y in acs) / 5 * 10_000)
