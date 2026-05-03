from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_21599.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cl1 = [d for d in dots if d[1] < -6]
cl2 = [d for d in dots if (d[1] < 10 * d[0] / 12 - 10) and d[1] > -6]
cl3 = [d for d in dots if d[1] > 10 * d[0] / 12 - 10 and d[1] > -6]
cls = [cl1, cl2, cl3]

cs = [center(cl) for cl in cls]

print(sum(x for x, y in cs) / len(cs) * 10_000)
print(sum(y for x, y in cs) / len(cs) * 10_000)


with open(r'.\files\27_B_21599.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cl1 = [d for d in dots if d[1] < -5]
cl2 = [d for d in dots if (d[1] < d[0]) and d[1] > -5]
cl3 = [d for d in dots if (d[1] > d[0]) and (d[1] < 10 * d[0] / 7 + 10)]
cl4 = [d for d in dots if (d[1] > 10 * d[0] / 7 + 10) and d[0] > -10]
cl5 = [d for d in dots if d[0] < -10 and d[1] > -19 / 12 * d[0] - 19]
cl6 = [d for d in dots if d[1] < -19 / 12 * d[0] - 19]
cls = [cl1, cl2, cl3, cl4, cl5, cl6]

cs = [center(cl) for cl in cls]
print(sum(x for x, y in cs) / len(cs) * 10_000)
print(sum(y for x, y in cs) / len(cs) * 10_000)
