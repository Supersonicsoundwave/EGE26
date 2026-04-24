from math import dist
from itertools import combinations


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_B_28766.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[0] == 'Z' and data[2:] == 'I':
            stars += [list(map(float, (x, y)))]

cl1 = [[d for d in dots if d[1] > 23],
       [s for s in stars if s[1] > 23]]
cl2 = [[d for d in dots if 16 < d[1] < 23],
       [s for s in stars if 16 < s[1] < 23]]
cl3 = [[d for d in dots if d[1] < 16],
       [s for s in stars if s[1] < 16]]
cls = [cl1, cl2, cl3]

B1 = []
for cl in cls:
    B1 += [dist(s1, s2) for s1, s2 in combinations(cl[1], 2)]

B2 = dist(center(min(cls, key=lambda x: len(x[1]))[0]), center(max(cls, key=lambda x: len(x[1]))[0]))

print(min(B1) * 10_000, B2 * 10_000)
