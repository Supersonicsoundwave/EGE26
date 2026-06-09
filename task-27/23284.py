from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_23284.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cl1 = [d for d in dots if d[1] > 15]
cl2 = [d for d in dots if d[1] < 15]
cl1_cen = center(cl1)
cl2_cen = center(cl2)
A1 = cl1_cen[0] + cl2_cen[0]
A2 = cl1_cen[1] + cl2_cen[1]


with open(r'.\files\27_B_23284.txt') as file:
    dots = [list(map(float, line.replace(',', '.').split())) for line in file]

cl1 = center([d for d in dots if 20 < d[0] < 30])
cl2 = center([d for d in dots if 10 < d[0] < 20])
cl3 = center([d for d in dots if 0 < d[0] < 10])
B1 = min(dist(cl1, cl2), dist(cl2, cl3), dist(cl1, cl3))
B2 = max(dist(cl1, cl2), dist(cl2, cl3), dist(cl1, cl3))

print(A1 * 10_000, A2 * 10_000)
print(B1 * 10_000, B2 * 10_000)
