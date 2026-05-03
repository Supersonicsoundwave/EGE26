from math import dist
from itertools import combinations


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_B_29357.txt') as file:
    dots = []
    Ostars = []
    Ystars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[0] == 'K' and data[2:] == 'III':
            Ostars += [list(map(float, (x, y)))]
        if data[0] == 'G' and data[2:] == 'V':
            Ystars += [list(map(float, (x, y)))]

cl1 = [[d for d in dots if d[0] > 16],
       [d for d in Ostars if d[0] > 16],
       [d for d in Ystars if d[0] > 16]]

cl2 = [[d for d in dots if d[0] < 16 and d[1] > 30],
       [d for d in Ostars if d[0] < 16 and d[1] > 30],
       [d for d in Ystars if d[0] < 16 and d[1] > 30]]

cl3 = [[d for d in dots if d[1] < 30],
       [d for d in Ostars if d[1] < 30],
       [d for d in Ystars if d[1] < 30]]


min_cen = center(min(cl1, cl2, cl3, key=lambda x: len(x[1]))[0])
max_cen = center(max(cl1, cl2, cl3, key=lambda x: len(x[1]))[0])
B1 = dist(min_cen, max_cen)

B2 = max(dist(y1, y2) for cl in (cl1, cl2, cl3) for y1, y2 in combinations(cl[2], 2))

print(B1 * 10_000, B2 * 10_000)
