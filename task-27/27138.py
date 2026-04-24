from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27A_27138.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cl1 = [d for d in dots if d[1] > 0]
cl2 = [d for d in dots if d[1] < 0]

cen1 = center(cl1)
cen2 = center(cl2)

print(abs(cen1[0] - cen2[0]) * 10_000)
print(abs(cen1[1] - cen2[1]) * 10_000)


with open(r'.\files\27B_27138.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cl1 = [d for d in dots if d[1] > 0 and d[0] < -40]
cl2 = [d for d in dots if d[1] > 0 and d[0] > 20]
cl3 = [d for d in dots if d[1] < -20]
cls = sorted([cl1, cl2, cl3], key=len)

print(max(cls[1])[0] * 10_000)

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
