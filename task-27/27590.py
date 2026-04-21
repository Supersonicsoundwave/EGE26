from math import dist


def anticenter(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return max(res)[1]


with open(r'.\files\27A_27590.txt') as file:
    data = [list(map(float, line.replace(',', '.').split())) for line in file]

cl1A = [dot for dot in data if dot[1] < 10]
cl2A = [dot for dot in data if dot[1] > 10]

anticen1A = anticenter(cl1A)
anticen2A = anticenter(cl2A)

print((anticen2A[0] + anticen2A[1]) * 10_000)
print((anticen1A[0] + anticen1A[1]) * 10_000)


with open(r'.\files\27B_27590.txt') as file:
    data = [list(map(float, line.replace(',', '.').split())) for line in file]

cl1B = [dot for dot in data if dot[0] > 8 and dot[1] < 20]
cl2B = [dot for dot in data if dot[0] < 18 and 20 < dot[1] < 30]
cl3B = [dot for dot in data if dot[0] > 18 and 20 < dot[1] < 30]

anticen1B = anticenter(cl1B)
anticen2B = anticenter(cl2B)
anticen3B = anticenter(cl3B)
acs = [anticen1B, anticen2B, anticen3B]

print(max(acs, key=lambda x: dist(x, (0, 0)))[0] * 10_000)
print(min(acs, key=lambda x: dist(x, (0, 0)))[1] * 10_000)
